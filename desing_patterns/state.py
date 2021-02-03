from __future__ import annotations
from abc import ABC, abstractmethod


class OrderState(ABC):
    def __init__(self, order: Orderr) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None: pass

    @abstractmethod
    def approve(self) -> None: pass

    @abstractmethod
    def reject(self) -> None: pass

class Orderr:
    """Context"""
    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        self.state.pending()    
    
    def approve(self) -> None:
        self.state.approve()    

    def reject(self) -> None:
        self.state.reject()

class PaymentPending(OrderState):
    def pending(self) -> None:
        print('Pagamento ja pendente, não posso fazer nada.')    
    
    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print('Pagamento aprovado')    

    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado')

class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print('Pagamento pendente')    
    
    def approve(self) -> None:
        print('Pagamento ja aprovado, não posso fazer nada.')    
    
    def reject(self) -> None:
        self.order.state = PaymentReject(self.order)
        print('Pagamento recusado') 

class PaymentReject(OrderState):
    def pending(self) -> None:
        self.recuse()   
    
    def approve(self) -> None:
        self.recuse()   
    
    def reject(self) -> None:
        self.recuse()

    def recuse(self) -> None:
        print('Pagamento recusado, sem permissão para operação')

