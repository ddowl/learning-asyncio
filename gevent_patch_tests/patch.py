def patch_all(**kwargs):
    import psycogreen.gevent
    from gevent import monkey as gevent_monkey

    gevent_monkey.patch_all(**kwargs)
    psycogreen.gevent.patch_psycopg()