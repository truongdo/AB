#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gluon import *
from gluon.sql import Rows
import abc


class AudioUtter():
    def __init__(self, id, name, text, audio_path_1, method_1,
                 audio_path_2, method_2, audio_path_ref=None, method_ref=None):
        self.id = id
        self.name = name
        self.text = text
        self.audio_path_1 = audio_path_1
        self.method_1 = method_1
        self.audio_path_2 = audio_path_2
        self.method_2 = method_2
        self.audio_path_ref = audio_path_ref
        self.method_ref = method_ref

    @staticmethod
    def from_record(record):
        return AudioUtter(record.id, record.f_name, record.f_text,
                          record.f_audio_path_1, record.f_method_1,
                          record.f_audio_path_2, record.f_method_2,
                          record.f_audio_path_ref, record.f_method_ref,
                          )

    def gen_html(self, request, autoplay=False):
        audio_1 = correct_path(request, self.audio_path_1)
        audio_2 = correct_path(request, self.audio_path_2)
        audio_ref = None
        if self.audio_path_ref and self.audio_path_ref != "None":
            audio_ref = correct_path(request, self.audio_path_ref) 
        
        data_audio = [audio_1, audio_2, audio_ref]
        data_method = [self.method_1, self.method_2, self.method_ref]
        
        rows = []
        for idx, x in enumerate(data_audio):
            if x and idx < 2:
                if autoplay:
                    rows.append(TR(
                                TD(), TD(XML("<audio id=\"audio_play\" controls autoplay src=\"%s\"></audio>" % x)),
                                TD(), TD(INPUT(_type="radio", _name="cb", _value=data_method[idx]))
                                )
                               )
                else:
                    rows.append(TR(
                                TD(), TD(XML("<audio id=\"audio_play\" controls src=\"%s\"></audio>" % x)),
                                TD(), TD(INPUT(_type="radio", _name="cb", _value=data_method[idx]))
                                )
                               )
            if idx == 2 and x:
                    rows.append(TR(
                                  TD(
                                    XML("<font color=\"red\"> <b>Reference<b> </font> " )
                                  ),
                                  TD(
                                    XML("<audio id=\"audio_play\" controls autoplay src=\"%s\"></audio>" % data_audio[2])
                                  ),
                                )
                               )
        rows.reverse()
        html = TABLE(*rows)    
        return html


    def update_result(self, result):
        self.result = result

    def save2db(self):
        return

    def gen_check_box_nature(self):
        radio = []
        for i in range(1,4):
            radio.append(TD(INPUT(_type="radio",_name="cb_"+str(self.id),_value=i)+LABEL(i)))
        return radio

    def gen_option_box(self):
        radio = []
        for i in range(1,4):
            radio.append(TD(INPUT(_type="radio",_name="cb_"+str(self.id),_value=i)+LABEL(i)))
        return radio


class ResultTable:
    def __init__(self, db):
        self.db = db
        self.table = self.db.t_result

    def find_by_id(self,id, uid):
        row = self.db((self.table.f_utt_id == id) & (self.table.f_user_id == uid)).select(self.table.ALL).first()
        if row:
            return row.f_result
        else:
            return None

    def find_by_user_id(self, user_id, filter=None):
        if filter:
            row = self.db(self.table.f_user_id == user_id & filter).select(self.table.ALL)
        else:
            row = self.db(self.table.f_user_id == user_id).select(self.table.ALL)
        return row

    def save_by_utt(self, utt, user_id):
        utt_id = self.table.update_or_insert((self.table.f_utt_id==utt.id) & \
                    (self.table.f_user_id == user_id), f_utt_id=utt.id, f_user_id=user_id, f_score=int(utt.score))
        return utt_id

    def save(self,utt_id, name, test_set, user_id, result, compare_method):
        utt_id = self.table.update_or_insert((self.table.f_utt_id==utt_id) & \
                        (self.table.f_user_id == user_id), f_utt_id=utt_id, f_test_set_id=test_set, f_name=name, f_user_id=user_id,\
                        f_result=result, f_systems=compare_method)
        return utt_id


class DbHelper:
    def __init__(self, db):
        self.db = db
        self.t_result = ResultTable(db)

    def fetch_table(self, table):
        records = self.db(table).select(table.ALL)
        return records

    def exe_query_on_table(self, table, query=None, **_filter):
        """
        @param record must have id field
        """
        records = self.db(query).select(table.ALL, **_filter).first()

    def mk_fetcher(self, query=None):
        """
        @param query
        @return fetcher function which can be used without arguments, or with limitby arguments
        @example: fet = mk_fetcher(db.t_utt.f_test_type == "a", db.t_utt); fet(); fet(limitby=(0,1))
        """

        def fetcher(*args, **kwargs):
            return self.db(query).select(*args, **kwargs)
        return fetcher


def record2object(records, obj):
    if isinstance(records, Rows):
        out = []
        for rec in records:
            out.append(obj.from_record(rec))
        return out
    else:
        return obj.from_record(records)

def correct_path(request, fname):
    addr='%s://%s' % (request.env.wsgi_url_scheme, request.env.http_host)
    wav=addr+URL(r=request,c='static/wav',f=fname)
    return wav

def setup_multi_page(page_num=None):
    if page_num: page=int(page_num)
    else: page=0
    items_per_page=1
    limitby=(page*items_per_page,(page+1)*items_per_page+1)
    return limitby, items_per_page

def get_all_row(db, table, limitby=None):
    records = db.select(table.ALL, limitby=limitby)
    for record in records:
        yield record

def get_row(db, table):
    return db.select(table.ALL).first()

def get_utt(db, table):
    return Utter.from_record(get_row(db, table))

def get_all_utt(db, table, limitby=None):
    for row in get_all_row(db, table, limitby):
        yield Utter.from_record(row)

def update_tts_result(db, d):
    utt_id = db.t_tts_result.update_or_insert((db.t_tts_result.f_utt_id==d["utt_id"]), f_utt_id=d["utt_id"], f_user_id=d["uid"],\
                             f_test_type=d["test_type"], f_system=d["system"],\
                             f_result=d["result"])
    return utt_id

def check_update(db, table_name, vars):
    if table_name == "t_tts_result":
        if "test_type" in vars:
            if vars["test_type"] == "MR-HSMM":
                update_tts_result(db, vars)
                return True
    return False
