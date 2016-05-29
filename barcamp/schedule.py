# coding: utf-8

"""
    Schedule settings
"""

from datetime import datetime


schedule = {
    'YEAR': '2016',
    'YEAR_ARCHIVE': ['2013', '2014', '2015'],
    'YEAR_ENABLED': ['2016'],
    'YEAR_SCHEDULE': {
        '2016': {
            'DATE': datetime(2016, 6, 4),
            'STAGES': {
                'PREVIEW': {
                    'from': datetime(1970, 1, 1),
                    'to': datetime(2016, 3, 12),
                },
                'CALL-FOR-PAPERS': {
                    'from': datetime(2016, 3, 13),
                    'to': datetime(2016, 5, 21),
                },
                'CALL-FOR-WORKSHOPS': {
                    'from': datetime(2016, 4, 10),
                    'to': datetime(2016, 4, 24),
                },
                'VOTING': {
                    'from': datetime(2016, 5, 1),
                    'to': datetime(2016, 5, 21),
                },
                'USERS': {
                    'from': datetime(2016, 5, 1),
                    'to': datetime(2016, 6, 4),
                },
                'T-SHIRTS': {
                    'from': datetime(2016, 4, 22),
                    'to': datetime(2016, 5, 13),
                },
                'PROGRAM': {
                    'from': datetime(2016, 5, 29),
                    'to': datetime(2020, 12, 31),
                },
                'PROGRAM-MENU': {
                    'from': datetime(2016, 5, 29),
                    'to': datetime(2020, 6, 4),
                },
            },
        },
        '2017': {
            'DATE': datetime(2017, 6, 3),
            'STAGES': {
                'PREVIEW': {
                    'from': datetime(1970, 1, 1),
                    'to': datetime(2017, 3, 11),
                },
            },
        },
    },
}