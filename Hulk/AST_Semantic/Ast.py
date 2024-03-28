import cmp.visitor as visitor
from abc import ABC, abstractmethod
class Node:


    def evaluate(self):
        raise NotImplementedError()


class ProgramNode(Node):
    def __init__(self, statements):
        self.statements = statements


class ParameterNode(Node):
    pass

class ProtocolMethodNode(Node):
    pass

class StatementNode(Node):
    pass


class ExpressionNode(StatementNode):
    pass

class TypeNode(StatementNode):
    pass


class ProtocolNode(StatementNode):
    pass

class ExpressionNode(StatementNode):
    pass

## Menor priopridad

class LetNode(SimpleExpressionNode):
    pass

class IfElseExpression(SimpleExpressionNode):
    pass

class DestructiveExpression(SimpleExpressionNode):
    pass

class whileNode(SimpleExpressionNode):
    pass

class forNode(SimpleExpressionNode):
    pass

class newNode(SimpleExpressionNode):
    pass

#Operaciones

class OrAndExpression(SimpleExpressionNode):
    pass

class NotExpression(SimpleExpressionNode):
    pass

class ComparationExpression(SimpleExpressionNode):
    pass

class IsExpression(SimpleExpressionNode):
    pass

class StringConcatenationNode(SimpleExpressionNode):
    pass

class AritmethicExpression(SimpleExpressionNode):
    pass

##Prioridad alta

class NumberNode(SimpleExpressionNode):
    pass

class StringNode(SimpleExpressionNode):
    pass

class BooleanNode(SimpleExpressionNode):
    pass

class Variable(SimpleExpressionNode):
    pass

class FunctionCallNode(SimpleExpressionNode):
    pass

class ClassAtributeCallNode(SimpleExpressionNode):
    pass

class ClassFunctionCallNode(SimpleExpressionNode):
    pass

class ListNode(SimpleExpressionNode):
    pass

class ImplicitListNode(SimpleExpressionNode):
    pass

class InexingNode(SimpleExpressionNode):
    pass

class asNode(SimpleExpressionNode):
    pass