from __future__ import division                                 
import numpy as np                                              
from pysd import functions                                      
from pysd import builder                                        
                                                                
class Components(builder.ComponentClass):                       
                                                                
    def regime_survival(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.total_cost()<self.regime_capability(), 1 , 0 ) 

    def regime_capability(self):
        """Type: Flow or Auxiliary
        """
        return 10 

    def total_cost(self):
        """Type: Flow or Auxiliary
        """
        return self.concessions()* self.concession_unit_cost()+ self.repressive_threat_tr()* self.repression_unit_cost() 

    def adjusting_concession_expectation(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest()>0 , self.concessions()* self.concession_fractional_adjustment()- self.expectation_of_concessions_needed(), 0 ) 

    def adjusting_repression_expectation(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest()>0 , self.repressive_threat_tr()* self.repression_fractional_adjustment()-\
		 self.expectation_of_repression_needed(), 0 ) 

    def concession_fractional_adjustment(self):
        """Type: Flow or Auxiliary
        """
        return 0.1 

    def concession_rate(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def concession_unit_cost(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def dconcessions_dt(self):                       
        return self.making_concessions()                           

    def concessions_init(self):                      
        return 0                           

    def concessions(self):                            
        """ Stock: concessions =                      
                 self.making_concessions()                          
                                             
        Initial Value: 0                    
        Do not overwrite this function       
        """                                  
        return self.state["concessions"]              
                                             
    def dexpectation_of_concessions_needed_dt(self):                       
        return self.adjusting_concession_expectation()                           

    def expectation_of_concessions_needed_init(self):                      
        return 1                           

    def expectation_of_concessions_needed(self):                            
        """ Stock: expectation_of_concessions_needed =                      
                 self.adjusting_concession_expectation()                          
                                             
        Initial Value: 1                    
        Do not overwrite this function       
        """                                  
        return self.state["expectation_of_concessions_needed"]              
                                             
    def dexpectation_of_repression_needed_dt(self):                       
        return self.adjusting_repression_expectation()                           

    def expectation_of_repression_needed_init(self):                      
        return 1                           

    def expectation_of_repression_needed(self):                            
        """ Stock: expectation_of_repression_needed =                      
                 self.adjusting_repression_expectation()                          
                                             
        Initial Value: 1                    
        Do not overwrite this function       
        """                                  
        return self.state["expectation_of_repression_needed"]              
                                             
    def initial_level_of_current_threat(self):
        """Type: Flow or Auxiliary
        """
        return 5 

    def making_concessions(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest()>0 , self.functions.if_then_else(self.preference_for_repression()<0, self.concession_rate(), 0 ) , 0 ) 

    def making_threats(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest()>0, self.functions.if_then_else(self.preference_for_repression()>=0 , self.threat_rate(), 0 ) , 0 ) 

    def preference_for_repression(self):
        """Type: Flow or Auxiliary
        """
        return (self.expectation_of_concessions_needed()* self.concession_unit_cost()- self.expectation_of_repression_needed()* self.repression_unit_cost()) / (self.expectation_of_repression_needed()* self.repression_unit_cost()) 

    def protest(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.expected_net_gain_from_protest_g()>0, 1 , 0 ) 

    def repression_fractional_adjustment(self):
        """Type: Flow or Auxiliary
        """
        return 0.1 

    def repression_unit_cost(self):
        """Type: Flow or Auxiliary
        """
        return 2 

    def drepressive_threat_tr_dt(self):                       
        return self.making_threats()                           

    def repressive_threat_tr_init(self):                      
        return 0                           

    def repressive_threat_tr(self):                            
        """ Stock: repressive_threat_tr =                      
                 self.making_threats()                          
                                             
        Initial Value: 0                    
        Do not overwrite this function       
        """                                  
        return self.state["repressive_threat_tr"]              
                                             
    def threat_rate(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def cost_of_protest_c(self):
        """Type: Flow or Auxiliary
        """
        return self.repressive_threat_tr() 

    def current_threat_tc(self):
        """Type: Flow or Auxiliary
        """
        return self.initial_level_of_current_threat()- self.concessions() 

    def gains_that_would_result_from_success_v(self):
        """Type: Flow or Auxiliary
        """
        return self.new_advantages_a()+ self.current_threat_tc() 

    def new_advantages_a(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def popular_support_k2(self):
        """Type: Flow or Auxiliary
        """
        return 0.1667 

    def probability_of_success_o(self):
        """Type: Flow or Auxiliary
        """
        return self.state_weakness_k1()+ self.popular_support_k2()+ self.strength_of_nonstate_allies_k3() 

    def strength_of_nonstate_allies_k3(self):
        """Type: Flow or Auxiliary
        """
        return 0.1667 

    def state_weakness_k1(self):
        """Type: Flow or Auxiliary
        """
        return 0.1666 

    def expected_net_gain_from_protest_g(self):
        """Type: Flow or Auxiliary
        """
        return (self.gains_that_would_result_from_success_v()* self.probability_of_success_o()) - self.cost_of_protest_c() 

    def final_time(self):
        """Type: Flow or Auxiliary
        """
        return 10 

    def initial_time(self):
        """Type: Flow or Auxiliary
        """
        return 0 

    def saveper(self):
        """Type: Flow or Auxiliary
        """
        return self.time_step() 

    def time_step(self):
        """Type: Flow or Auxiliary
        """
        return 0.03125 

