### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_data',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_test_set_id', type='string',
          label=T('Test Set ID')),
    Field('f_system', type='string',
          label=T('System')),
    Field('f_text', type='string',
          label=T('Text')),
    Field('f_audio_path', type='string',
          label=T('Audio Path')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_data_archive',db.t_data,Field('current_record','reference t_data',readable=False,writable=False))

########################################
db.define_table('t_result',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_test_set_id', type='string',
          label=T('Test Set ID')),
    Field('f_system', type='string',
          label=T('System')),
    Field('f_utt_id', type='integer',
          label=T('Utt Id')),
    Field('f_user_id', type='integer',
          label=T('User Id')),
    Field('f_score', type='integer',
          label=T('Score')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

########################################
db.define_table('t_subject',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_age', type='string',
          label=T('Age')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_result_archive',db.t_result,Field('current_record','reference t_result',readable=False,writable=False))
