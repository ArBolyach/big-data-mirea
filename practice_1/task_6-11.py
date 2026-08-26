# Скачать и загрузить данные о стоимости домов в калифорнии,
# используя библиотеку sklearn. 

from sklearn.datasets import fetch_california_housing
import pandas

data:pandas.DataFrame = fetch_california_housing(as_frame=True).frame

# Использовать метод info().
print("Method info()")
print(data.info())

# Узнать, есть ли пропущенные значения, используя isna().sum().
print("  ")
print("Method isna().sum()")
print(data.isna().sum())

# Вывести записи, где средний возраст домов в районе более 50 лет и
# население более 2500 человек, используя метод loc().

print("  ")
print("Method loc()")
print(data.loc[(data["HouseAge"] > 50) & (data["Population"] > 2500)])

# Узнать максимальное и минимальное значения медианной
# стоимости дома.

print("  ")
print("Max and min med home price")
print("max: " + str(data["MedHouseVal"].max()))
print("min: " + str(data["MedHouseVal"].min()))

# Используя метод apply(), вывести на экран название признака и его
# среднее значение.

print("  ")
print("method apply()")
data.apply(lambda column: print(column.name, column.mean()))
