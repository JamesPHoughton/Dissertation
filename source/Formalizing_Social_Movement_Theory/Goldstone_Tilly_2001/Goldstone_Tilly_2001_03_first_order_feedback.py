from __future__ import division                                 
import numpy as np                                              
from pysd import functions                                      
from pysd import builder                                        
                                                                
class Components(builder.ComponentClass):                       
                                                                
    def ability_to_make_concessions(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def ability_to_repress(self):
        """Type: Flow or Auxiliary
        """
        return 3 

    def adjusting_repression(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest(), self.functions.if_then_else(self.manifest_repressive_threat_tr()<self.ability_to_repress(), self.agressiveness_of_response()* self.bias_towards_repression(), 0 ) , 0 ) 

    def agressiveness_of_response(self):
        """Type: Flow or Auxiliary
        """
        return 0.25 

    def bias_towards_repression(self):
        """Type: Flow or Auxiliary
        """
        return self.cost_per_unit_concession()/ (self.cost_per_unit_concession()+ self.cost_per_unit_repression()) 

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
                                             
    def cost_per_unit_concession(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def cost_per_unit_repression(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def cost_to_regime(self):
        """Type: Flow or Auxiliary
        """
        return self.concessions()* self.cost_per_unit_concession()+ self.manifest_repressive_threat_tr()* self.cost_per_unit_repression() 

    def gains_that_would_result_from_success_v(self):
        """Type: Flow or Auxiliary
        """
        return self.percieved_advantages_of_protest_a()+ self.percieved_current_threat() 

    def making_concessions(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.protest(), self.functions.if_then_else(self.concessions()<self.ability_to_make_concessions(), self.agressiveness_of_response()* (1-self.bias_towards_repression()) , 0 ) , 0 ) 

    def manifest_current_threat_tc(self):
        """Type: Flow or Auxiliary
        """
        return self.starting_current_threat_level()- self.concessions() 

    def percieved_repressive_threat_tr(self):
        """Type: Flow or Auxiliary
        """
        return self.manifest_repressive_threat_tr() 

    def opposition_percieved_gains_to_protest_g(self):
        """Type: Flow or Auxiliary
        """
        return (self.gains_that_would_result_from_success_v()* self.opposition_percieved_probability_of_success_opportunity_o()) - self.percieved_repressive_threat_tr() 

    def opposition_percieved_probability_of_success_opportunity_o(self):
        """Type: Flow or Auxiliary
        """
        return self.state_weakness_k1()+ self.popular_support_for_protest_k2()+ self.strength_of_nonstate_allies_k3() 

    def percieved_advantages_of_protest_a(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def percieved_current_threat(self):
        """Type: Flow or Auxiliary
        """
        return self.manifest_current_threat_tc() 

    def strength_of_nonstate_allies_k3(self):
        """Type: Flow or Auxiliary
        """
        return 0.1667 

    def popular_support_for_protest_k2(self):
        """Type: Flow or Auxiliary
        """
        return 0.1667 

    def state_weakness_k1(self):
        """Type: Flow or Auxiliary
        """
        return 0.1666 

    def starting_current_threat_level(self):
        """Type: Flow or Auxiliary
        """
        return 1 

    def dmanifest_repressive_threat_tr_dt(self):                       
        return self.adjusting_repression()                           

    def manifest_repressive_threat_tr_init(self):                      
        return 1                           

    def manifest_repressive_threat_tr(self):                            
        """ Stock: manifest_repressive_threat_tr =                      
                 self.adjusting_repression()                          
                                             
        Initial Value: 1                    
        Do not overwrite this function       
        """                                  
        return self.state["manifest_repressive_threat_tr"]              
                                             
    def protest(self):
        """Type: Flow or Auxiliary
        """
        return self.functions.if_then_else(self.opposition_percieved_gains_to_protest_g()>0, 1 , 0 ) 

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

