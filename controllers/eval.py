# -*- coding: utf-8 -*-
# try something like
import myutils
from gluon.sql import Row
from gluon.debug import dbg
db_helper = myutils.DbHelper(db)

def init_multi_page(page):
    multi_page = None
    multi_page, items_per_page = myutils.setup_multi_page(page)
    return multi_page, items_per_page

def check_update_record(vars):
    if "utt_id" in vars:
        if "score_select" in vars:
            res_uttid = db_helper.t_result.save(vars.utt_id, vars.name,
                        vars.test_set, vars.user_id, vars.score_select, system=vars.system)
    else:
        return 1
    return 0

def index():
    from random import shuffle
    page = int(request.args[0])

    update_s = check_update_record(request.vars)
    if update_s == 2:
        response.flash=T("Input difference score for each utterance")
    elif update_s == 3:
        response.flash=T("Input values")
    elif update_s == 1:
        do_nothing = 1
    else:
        redirect(URL('eval','index', args=[page+1],vars=dict(test_set=request.vars.test_set,\
                                                             user_id=request.vars.user_id)))
    litmitby, items_per_page = init_multi_page(page)

    finish_item = [x.f_name for x in db_helper.t_result.find_by_user_id(int(request.vars.user_id))]
    utt_fetcher = db_helper.mk_fetcher((db.t_data.f_test_set_id == request.vars.test_set) & \
                                        (~db.t_data.f_name.belongs(finish_item)))
    utt_records = utt_fetcher(db.t_data.ALL)
    all_utts = myutils.record2object(utt_records, myutils.AudioUtter)
    # dbg.set_trace()
    #shuffle(all_utts)
    rows = []
    for utt in all_utts:
        form = FORM(
            TABLE(
                TR(TD(utt.text)),
                TR(TD(utt.gen_htmlwav(request))),
                SELECT(_name='score_select', *[OPTION(i, _value=i) for i in range(1, 6)])
            ),BR(),
            INPUT(_type='submit'), _action='', _method='post',_id="abcde",\
            hidden=dict(utt_id=utt.id, name=utt.name, system=utt.system),
        )
        a=Row()
        a.__setattr__("form",form)
        rows.append(a)
    return dict(rows=rows, page=page,items_per_page=items_per_page, finish_item=len(finish_item))
