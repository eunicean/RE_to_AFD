import createTree as ct
import createNFA as nfa
import createDFA as dfa
import re_to_postfix as pos
import simulateNFA as simNFA
import simulateDFA as simDFA

with open("regular_expressions.txt", "r", encoding="UTF-8") as file:
    expressions = file.readlines()

keyLoop = True

while keyLoop:
    for i, expression in enumerate(expressions):
        print(f"{i + 1}. {expression}")
            
    option = input("Ingresa el número con la expresión a operar: ")
    chain = input("Ingresa la cadena para realizar la simulación: ")

    postfixExpression = pos.to_postfix(expressions[int(option) - 1].strip())

    syntaxTree = ct.createTree(postfixExpression)

    Treefilename = f"syntaxTree"
    automatonFilename = f"nfa"
    automatonDFilename = f"dfa"

    ct.createGraph(syntaxTree, Treefilename)

    nonDeterministicAutomaton, alphabet = nfa.generateAutomatonFromTree(syntaxTree)
    nfa.createGraph(nonDeterministicAutomaton, automatonFilename)
    print("Autómata Finito No Determinista creado. \n")
    print(simNFA.chainSimulation(chain, nonDeterministicAutomaton, alphabet), postfixExpression, "\n\n")

    deterministicAutomaton = dfa.getNewStates(nonDeterministicAutomaton, alphabet)
    dfa.createGraph(deterministicAutomaton, automatonDFilename)
    print("Autómata Finito Determinista creado. \n")
    print(simDFA.chainSimulation(chain, deterministicAutomaton, alphabet), postfixExpression, "\n\n")

    input("Presiona ENTER para continuar.")

# Implementación de algoritmos obtenidas de proyecto anterior: https://github.com/DANdelion-0908/Proyecto1-Teor-a-de-la-Computaci-n.git