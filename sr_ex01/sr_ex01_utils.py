values = {
    # Интенсивность отказов lambda_0, 10e-6 1/час
    "резисторы": {
        "МЛТ": {
            "0.25": 0.4,    "0.5":  0.5,    "1":    1.0,    "2":    1.6
        },
        "ТВО": {
            "0.25": 0.4,    "0.5":  0.45,   "1":    0.8,    "2":    1.4,
            "5":    2.2,    "10":   3.0,    "20":   4.0,    "60":   6.0
        },
        "МОУ": {
            "0.25": 0.5,    "0.5":  0.55,   "1":    1.1,    "2":    1.5,
            "5":    2.3,    "10":   3.1,    "25":   4.2,    "50":   5.5,
            "100":  10
        },
        "МУН": {
            "0.25": 0.6,    "0.5":  0.6,   "1":    1.2,    "2":    2.0
        },
        "УНУ": {
            "0.25": 0.6,    "0.5":  0.7,   "1":    1.2,    "2":    1.7,
            "5":    2.3,    "10":   3.0,   "25":   4.8,    "50":   8.0,
            "100":  12
        },
        "КЭВ": {
            "0.25": 0.6,    "0.5":  0.75,   "1":    1.3,    "2":    1.75,
            "5":    2.4,    "10":   3.1,    "25":   5.0
        },
        "ВС": {
            "0.25": 0.7,   "0.5":  0.8,   "1":    1.35,    "2":    1.8,
            "5":    2.5,   "10":   3.3
        },
        "УЛИ": {
            "0.25": 0.6,   "0.5":  0.65,  "1":    1.3
        },
        "БЛП": {
            "0.25": 0.7,   "0.5":  0.75,  "1":    1.4
        },
        "СПО": {
            "0.25": 0.6,   "0.5":  0.7,   "1":    1.15,    "2":    1.8
        },
        "СП": {
            "0.25": 0.7,   "0.5":  0.8,   "1":    1.3,    "2":    2.0
        },
        "ПТН": {
            "0.5":  1.1,    "1":    1.4,    "2":    1.8
        },
        "ПКВ": {
            "0.5":  1.2,    "1":    1.5,    "2":    2.0,     "5":    2.5
        },
        "ПЭВ": {
            "0.5":  1.2,    "1":    1.5,    "2":    2.0,     "5":    2.5,
            "10":   3.2,    "15":   3.5,   "25":   4.5,    "30":   5.0,
            "50":   5.6,    "75":   8.0,   "100":  12
        },
        "ПТП": {
            "1":  2.2,   "2":    2.6,   "5":    3.0
        },
        "РП": {
            "2":    3.0,    "25":   4.7,    "75":   8.5
        }
    },

    "конденсаторы": {
        "бумажные":                         1.8,
        "металлобумажные":                  2.0,
        "слюдяные":                         1.2,
        "стеклянные":                       1.6,
        "керамические":                     1.4,
        "пленочные":                        2.0,
        "электрические": {
            "алюминиевые":                  2.4,
            "танталовые":                   2.2
        }
    },

    "диоды": {
        "выпрямительные": {
            "точечные": {
                "германиевые":              0.7,
                "кремниевые":               2
            },
            "микроплоскостные":             0.7,
            "плоскостные": {
                "обычные":                  5,
                "повышенной надежности":    2.5
            },
            "повышенной мощности":          5
        },
        "импульсные": {
            "точечные":                     3,
            "плоскостные мезадиодны": {
                "германиевые":              2,
                "кремниевые":               2.5
            },
            "сплавные":                     0.6
        },
        "управляемые":                      5,
        "стабилитроны":                     5,
        "варикапы":                         5,
        "выпрямительные столбы":            5,
        "микромодульные": {
            "германиевые":                  4.2,
            "кремниевые":                   4.5
        }
    },

    "транзисторы" : {
        "маломощные": {
            "низкочастотные": {
                "германиевые":              3,
                "кремниевые":               4
            },
            "высокочастотные":              2.6
        },
        "мощные": {
            "высокочастотные": {
                "германиевые":              5,
                "кремниевые":               1.7
            },
            "низкочастотные":               4.6
        },
        "микромодульные":                   1
    },

    "трансформаторы": {
        "автотрансформаторы":               5.0,
        "силовые":                          3.0,
        "высоковольтные":                   4.0,
        "накальные":                        2.0,
        "импульсные":                       0.5,
    },

    "дроссели":                             1.0,
    
    "катушки": {
            "индуктивности":                0.5
    }
}