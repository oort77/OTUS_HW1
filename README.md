# OTUS_HW1
 OTUS homework 1 - gradient boosting algorithms
 
 **Домашнее задание 1. Чем лучше бустить? Тестируем алгоритмы бустинга в бою.**

Цель:
В этом домашнем задании вам предстоит провести детективную работу и узнать, какой же алгоритм бустинга работает лучше всего (конечно, применительно к конкретной задаче)

**Часть 1. EDA**

Выберите любой интересующий вас датасет по классификации или регрессии (можно взять из рекозитория https://archive.ics.uci.edu/ml/datasets.php, еще неплохие и востребованные на практике варианты - предсказание оттока пользователей https://www.kaggle.com/blastchar/telco-customer-churn или предсказание Customer Livetime Value (CLV или LTV) - https://www.kaggle.com/pankajjsh06/ibm-watson-marketing-customer-value-data
По выбранному датасету проведите EDA, познакомьтесь с признаками, посмотрите зависимости и т.д.

**Часть 2. Preprocessing & Feature Engineering**

Хотя цель этого задания - посмотреть на работу алгоритмов, тем не менее пропускать препроцессинг нельзя :)
Так что переведите категориальные переменные в уникальные лейблы при помощи LabelEncoder, попробуйте добавить новые переменные и выкинуть лишние и, наконец, разбейте данные на train-test.

**Часть 3. Who's the mightiest of them all?**

Постройте 4 варианта градиентного бустинга, используя значения гиперпараметров “из коробки”: реализация из sklearn, XGBoost, CatBoost, LightGBM. Проверьте качество на отложенной выборке, кто пока лидирует?

**Часть 4. Теперь проведите настройку гиперпараметров моделей на кросс-валидации.**

Можно настраивать только самые основные гиперпараметры - число итераций бустинга, max_features, subsample и т.д.
Снова проверьте качество уже настроенных моделей, кто, в итоге победил?

**Критерии оценки:**  

EDA для выбранного датасета - 1 балл
Preprocessing - 1 балл
Построение моделей из коробки и проверка качества - 4 балла
Настройка гиперпараметров моделей и проверка качества - 4 балла

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/oort77/OTUS_HW1/blob/main/notebooks/HW1_atom.ipynb)
