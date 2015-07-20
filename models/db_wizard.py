### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_data',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_test_set_id', type='string',
          label=T('Test Set ID')),
    Field('f_text', type='string',
          label=T('Text')),
    Field('f_audio_path_1', type='string',
          label=T('Audio Path 1')),
    Field('f_method_1', type='string',
          label=T('Method 1')),
    Field('f_audio_path_2', type='string',
          label=T('Audio Path 2')),
    Field('f_method_2', type='string',
          label=T('Method 2')),
    Field('f_audio_path_ref', type='string',
          label=T('Audio Path Reference')),
    Field('f_method_ref', type='string',
          label=T('Method Reference')),
    auth.signature,
    format='%(f_name)s',
    migrate=settings.migrate)

db.define_table('t_data_archive',db.t_data,Field('current_record','reference t_data',readable=False,writable=False))

########################################
db.define_table('t_result',
    Field('f_name', type='string',
          label=T('Name')),
    Field('f_systems', type='string',
          label=T('Compare systems')),
    Field('f_test_set_id', type='string',
          label=T('Test Set ID')),
    Field('f_utt_id', type='integer',
          label=T('Utt Id')),
    Field('f_user_id', type='integer',
          label=T('User Id')),
    Field('f_result', type='string',
          label=T('Result')),
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
