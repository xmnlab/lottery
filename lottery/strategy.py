"""

"""
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import random


class LoteryStrategyBase:
    """
    
    """
    data = None  # pd.DataFrame
    n_choices = 0
    n_picked = 0
    k_results = None  # list
    vmin = 0
    vmax = 0
    n_train = 0
    results = None  # list
    hits_to_win = None  # tuple
    
    def __init__(
        self, data: pd.DataFrame,
        n_picked: int, n_choices: int,
        vmin: int, vmax: int, n_train: int, hits_to_win: tuple
    ):
        """
        Data is the historical data of lotery's results
        """
        self.data = data
        self.n_picked = n_picked
        self.n_choices = n_choices
        self.vmin = vmin
        self.vmax = vmax
        self.n_train = n_train
        self.hits_to_win = hits_to_win
        
        self.k_results = list(range(n_picked))
        self.run()
        
    def check_hits(self, choice, result):
        """
        
        """
        result = set(choice) & set(result)
        return len(result)
    
    def pick_numbers(self):
        """
        
        """
        raise Exception('Override pick_number method.')
    
    def run(self):
        """
        
        """
        self.results = []
        k = self.k_results
        i_data = self.data[k].iloc
        n_train = self.n_train
        
        for i in range(self.data.shape[0] - n_train):
            df_train = i_data[i:i+n_train] 
            values_test = (
                i_data[i+n_train:i+n_train+1].values[0].tolist()
            )
            choice = self.pick_numbers(df_train)
            self.results.append(self.check_hits(choice, values_test))
    
    def plot_stats(self):
        """
        
        """
        df = pd.DataFrame({'results': self.results})
        df.hist(bins=20)
        plt.show()
        
    def stats(self):
        """
        
        """
        df = pd.DataFrame({'results': self.results})
        print(df.describe())
        
    def win_results(self):
        """
        
        """
        t = len(self.results)
        w = sum([1 if r in self.hits_to_win else 0 for r in self.results])
        return '%s/%s (%s %%)' % (w, t, (w/t)*100)
        
