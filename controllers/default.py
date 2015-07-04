# -*- coding: utf-8 -*-
### required - do no delete
import myutils
from gluon.sql import Row
from gluon.debug import dbg
db_helper = myutils.DbHelper(db)

def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires
def index():
    form = SQLFORM(db.t_subject)
    if form.validate():
        form.vars.id = db.t_subject.insert(**dict(form.vars))
        redirect(URL('default','test_list', vars=dict(user_id=form.vars.id)))

    utt_fetcher = db_helper.mk_fetcher()
    utt_records = utt_fetcher(db.t_subject.ALL)
    list_user = [(row.id, row.f_name, row.f_age) for row in utt_records]
    
    table_rows = []
    for user_id, name, age in list_user:
        table_rows.append(TR(MARKMIN("[[User - %s %s %s]]"
                                %(name, age, URL('default', 'test_list', vars=dict(user_id=user_id))))))
    html = TABLE(
            *table_rows
    )

    
    return dict(form=form, html=html)

def error():
    return dict()

@auth.requires_login()
def data_manage():
    check_del(request.vars, db.t_data)
    check_update("t_data")
    form = SQLFORM.smartgrid(db.t_data,onupdate=auth.archive)
    return dict(form=form, batch_add=gen_form("t_data"))

    # form = SQLFORM.smartgrid(db.t_data,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def result_manage():
    check_del(request.vars, db.t_result)
    form = SQLFORM.smartgrid(db.t_result,onupdate=auth.archive)
    return locals()

@auth.requires_login()
def user_manage():
    check_del(request.vars, db.t_subject)
    form = SQLFORM.smartgrid(db.t_subject,onupdate=auth.archive)
    return locals()

def test_list():
    utt_fetcher = db_helper.mk_fetcher()
    utt_records = utt_fetcher(db.t_data.f_test_set_id)
    list_test_set = sorted(set([row.f_test_set_id for row in utt_records]))
    
    table_rows = []
    for test_name in list_test_set:
        table_rows.append(TR(MARKMIN("[[Test set - %s %s]]"
                                %(test_name, URL('eval', 'index', args=[0], vars=dict(user_id=request.vars.user_id, test_set=test_name))))))
    html = TABLE(
            *table_rows
    )

    return dict(html=html)

def check_del(keys, table):
    if ("del_table"):
        if "del_table" in request.vars:
            del_table(table)

def del_table(table):
    table.truncate()

def check_update(table_name):
    if table_name in request.vars:
        for d in iter_data(request.vars[table_name]):
            if table_name == "t_data":
                update_record(d)

def update_record(d):
    parts = d.strip().split("|")
    if len(parts) < 7:
        return 0

    if len(parts) == 7:
        record_id = db.t_data.insert(f_name=parts[0], f_test_set_id=parts[1],\
            f_text=parts[2], \
            f_audio_path_1=parts[3], f_method_1=parts[4],
            f_audio_path_2=parts[5], f_method_2=parts[6],
            )
    elif len(parts) == 9:
        record_id = db.t_data.insert(f_name=parts[0], f_test_set_id=parts[1],\
            f_text=parts[2], \
            f_audio_path_1=parts[3], f_method_1=parts[4],
            f_audio_path_2=parts[5], f_method_2=parts[6],
            f_audio_path_ref=parts[7], f_method_ref=parts[8],
            )

    return record_id

def gen_form(table_name):
    if table_name == "t_data":
        hint = "utt_name|test_set_id|text|audio_path_1|method1|audio_path2|method2[|audio_path3|reference]"
    form = XML(INPUT(_type="button",_value="Batch add",_id="toggle_btn")+\
               FORM(TEXTAREA(_type="text",_name=table_name,_placeholder=hint),INPUT(_type="submit",_value="Submit"), _id="add_form"))
    return form

def iter_data(data):
    for line in data.split("\n"):
        line = line.strip()
        if line != "":
            yield line
