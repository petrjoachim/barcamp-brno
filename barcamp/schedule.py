# coding: utf-8

"""
    Schedule settings
"""

from datetime import datetime


schedule = {
    'YEAR': '2019',
    'LANDING_YEAR': '2019',
    'YEAR_ARCHIVE': ['2013', '2014', '2015', '2016', '2017', '2018'],
    'YEAR_ENABLED': ['2019'],
    'YEAR_SCHEDULE': {
        # '2016': {
        #     'DATE': datetime(2016, 6, 4),
        #     'STAGES': {
        #         'T-SHIRTS': {
        #             'from': datetime(2016, 4, 22),
        #             'to': datetime(2016, 5, 13),
        #         },
        #         'PROGRAM': {
        #             'from': datetime(2016, 5, 29),
        #             'to': datetime(2020, 12, 31),
        #         },
        #         'PROGRAM-MENU': {
        #             'from': datetime(2016, 5, 29),
        #             'to': datetime(2020, 6, 4),
        #         },
        #         'REVIEW-MENU': {
        #             'from': datetime(2016, 6, 15),
        #             'to': datetime(2020, 6, 4),
        #         }
        #     },
        # },
        '2019': {
            'DATE': datetime(2019, 10, 5),
            'STAGES': {
                'PREVIEW': {
                    'from': datetime(1970, 1, 1),
                    'to': datetime(2019, 6, 4, 16, 0),
                },
                'CALL-FOR-PAPERS': {
                    'from': datetime(2019, 6, 4, 16, 0),
                    'to': datetime(2019, 9, 3, 15, 0),
                },
                'CALL-FOR-WORKSHOPS': {
                    'from': datetime(2019, 6, 4, 16, 0),
                    'to': datetime(2019, 8, 31),
                },
                'VOTING': {
                    'from': datetime(2019, 9, 3, 16, 0),
                    'to': datetime(2019, 9, 28, 22, 0),
                },
                'PROGRAM': {
                    'from': datetime(2019, 9, 30, 16, 0),
                    'to': datetime(2021, 12, 31),
                },
                'WORKSHOPS-PROGRAM': {
                    'from': datetime(2019, 9, 26),
                    'to': datetime(2021, 12, 31),
                },
                'USERS': {
                    'from': datetime(2019, 9, 3, 16, 0),
                    'to': datetime(2019, 10, 4),
                },
            },

        },
    },
}
