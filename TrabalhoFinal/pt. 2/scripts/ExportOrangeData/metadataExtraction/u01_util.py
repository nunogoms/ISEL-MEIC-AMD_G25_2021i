# to use accented characters in the code
# -*- coding: cp1252 -*-
# ===============================
# author: Paulo Trigo Silva (PTS)
# since: SEP.2017
# version: v05 (Python3)
# ===============================


#_______________________________________________________________________________
# Some Utility Functions
def my_print( aStr ):
   separator = lambda x: "_" * len( x )
   print( separator( aStr ) )
   print( aStr )

def print_attributes (dataset) :
   variable_list = dataset.domain.attributes
   print(":: name (type): [value1, value2, ...]")

   nDisc = 0;
   nCont = 0;
   nStr = 0;
   for variable in variable_list:
      print("\n:: %s %s" % (variable.name, variable.TYPE_HEADERS)),
      if variable.is_discrete:
         print(": %s " % str(variable.values))
         nDisc += 1
      elif variable.is_continuous:
         nCont += 1
      else:
         nStr += 1

   my_print(">> Types: %d discrete, %d continuous <<" % (nDisc, nCont))


def print_class(dataset):
   # _______________________________________________________________________________
   # Class: name (type = discrete | continuous): <value1, value2, ...>
   the_class = dataset.domain.class_var
   my_print(">> Class <<")
   print(":: %s (%s): %s " % (the_class.name,
                              the_class.TYPE_HEADERS,
                              the_class.values))


