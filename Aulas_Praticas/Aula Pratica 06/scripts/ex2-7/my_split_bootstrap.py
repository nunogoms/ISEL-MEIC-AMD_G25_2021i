from abc import abstractmethod, ABC
from typing import List

from sklearn.utils import resample


class MyBootstrap( ABC ):
  @abstractmethod
  def get_seed(): pass


  def __init__( self, seed=None ):
    self.seed = seed
    self.reset_tt_split_indexes()


  def reset_tt_split_indexes( self ):
    self.tt_split_indexes = None


  # train|test split
  def split( self, X, y=None ):
    # if train|test split already exists, then return
    if self.tt_split_indexes != None:
      return self.tt_split_indexes

    #_____________________________
    # build a new train|test split
    dim_dataset = len( X )
    indexes = list( range( dim_dataset ) )

    # training set is created from resamples (samples with reposition)
    seed = self.get_seed()
    #print( "seed = ", seed )
    train_indexes = resample( indexes, n_samples=dim_dataset, random_state=seed )

    #testing set is created from individuals, i, not in training set


    #Ex5.b)

    test_indexes : List[int] = []
    for index in indexes :
      if not train_indexes.__contains__(index) :
        test_indexes.append(index)

    ########### ASK ###########
    #random.seed(seed)
    #test_indexes : List[int] = []
    #for index in indexes :
    #  if random.random() < (1/dim_dataset) :
    #    indexes.remove(index)
    #    test_indexes.append(index)

   # test_indexes = train_indexes

    self.tt_split_indexes = [ ( train_indexes, test_indexes ) ]
    return self.tt_split_indexes



#____
class MyBootstrapSplitOnce( MyBootstrap ):
  def get_seed( self ):
    return self.seed



#____
class MyBootstrapSplitRepeated( MyBootstrap ):
  def __init__( self, n_repeat, seed=None ):
    super().__init__( seed )
    self.n_repeat = n_repeat
    self.tt_split_repeated_indexes = None


  def get_seed( self ):
    seed_current = self.seed
    if self.seed != None: self.seed = self.seed  + 1
    return seed_current


  def split( self, X, y=None ):
    # if train|test split-repeated already exists, then return
    if self.tt_split_repeated_indexes != None:
      return self.tt_split_repeated_indexes

    #______________________________________
    # build a new train|test split-repeated
    self.tt_split_repeated_indexes = list()
    for i in range( self.n_repeat ):
      self.reset_tt_split_indexes()
      self.tt_split_repeated_indexes = self.tt_split_repeated_indexes + \
                                       super().split( X )
    return self.tt_split_repeated_indexes

