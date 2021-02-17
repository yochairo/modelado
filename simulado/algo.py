#!/usr/bin/python
# -*- coding: utf-8 -*-
#
#	==================
#	Algorítmo genético
#	==================
#
#	Autor
#	Miguel Ángel Maffet Wall
#	Junio 2017
#

#	Librerias
from pprint import pprint
import random
import numpy

#	Funciones
def ga_init(size):
   matrix = numpy.random.randint(10, size = (size,size))
   for x in range(0,size):
      matrix[x][x] = 0
   return matrix

def ga_table(matriz,size):
   table = []
   count = 1
   for x in range(0,size):
      for y in range(0,size):
         if matriz[x][y] != 0:
            table.append([count,x,y,matriz[x][y]])
            count = count + 1
   return table

def ga_init_mutation(size):
   reference = numpy.zeros(size, dtype=numpy.int)
   max_ones = random.randint(1,size)
   for x in range(0,max_ones):
      reference[random.randint(0,max_ones)] = 1
   return reference

def ga_mutation(ref,size):
   index = random.randint(0,size-1)
   ref[index] = abs(1-ref[index])
   return ref

def ga_fitness(ref,table):
   fitness = 0
   count = 0
   for x in ref:
      if x!=0:
         fitness = fitness + table[count][3]
      count = count + 1
   return fitness

def ga_min(array):
   current_value = array[0][0]
   current_index = 0
   min_index = 0
   for x in array:
      if x[0]<current_value:
         current_value = x[0]
         min_index = current_index
      current_index = current_index + 1
   return min_index


#	Main
def main():
   size = 5
   population = 20 #  1 + x
   matrix = ga_init(size)
   print ("La Matriz es:")
   pprint(matrix)
   print ("La tabla generada es:")
   table = ga_table(matrix,size)
   table_lenght = len(table)
   pprint(table)
   reference = ga_init_mutation(table_lenght)
   mutation = []
   mutation_results = []
   print ("Las mutaciones posibles son:")
   mutation.append(list(reference))
   mutation_results.append([ga_fitness(reference,table),0])
   for x in range(1,population+1):
      reference_aux = list(ga_mutation(reference,table_lenght))
      mutation.append(reference_aux[:])
      mutation_results.append([ga_fitness(reference_aux,table),x])
   pprint(mutation)
   pprint(mutation_results)

   winner = ga_min(mutation_results)
   print ("El mejor candidato es "+str(winner)+": ")
   print (mutation[winner])
   print ("Que tiene un costo mínimo de: ")
   print (mutation_results[winner][0])

 

main()