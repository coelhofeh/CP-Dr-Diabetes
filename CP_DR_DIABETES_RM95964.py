#RM95964 Felipe Matheus Coelho 
#CP Dr.diabétes - Machine Learning
from sklearn import tree #importa o módulo "tree" do Sklearn Árvore de Decisão
features = [[90, 120, 110], [95, 130, 140], [85, 125, 145], [110, 145, 135], [120, 160, 130], [125, 180, 160], [127, 200, 220], [130, 220, 240], [140, 215, 205]]
#labels = [Glicemia normal, Glicose diminuida, Diabétes Mellitus]
#A Glicemia normal será representada por 0, a Glicose diminuida será representado por 1, enquando a Diabétes Mellitus será representada por 2
labels = [0, 0, 0, 1, 1, 1, 2, 2, 2] #número de classes
classif = tree.DecisionTreeClassifier() #Classificador
classif.fit(features, labels)
jejum = float(input("Digite a taxa de glicemia no período de jejum:"))
tolerancia = float(input("Digite a taxa de glicemia nos períodos de pós sobrecarga:"))
diabetes = float(input("Digite a taxa de glicemia casual:"))
x = classif.predict([[jejum, tolerancia, diabetes]])
if x == 0:
    print("Glicemia Normal!")
elif x == 1:
    print("Tolerancia à glicose diminuída!")
else:
    print("Diabétes Mellitus!") 
#output
# [0]  or a