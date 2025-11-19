# Generated from ProductoPunto.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,11,62,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,2,1,2,1,2,1,2,1,3,1,3,1,
        3,1,3,1,4,1,4,1,4,1,4,5,4,36,8,4,10,4,12,4,39,9,4,1,4,1,4,1,5,1,
        5,1,5,1,5,1,6,1,6,1,6,5,6,50,8,6,10,6,12,6,53,9,6,1,7,1,7,1,7,1,
        7,1,7,1,7,1,7,1,7,0,0,8,0,2,4,6,8,10,12,14,0,0,55,0,16,1,0,0,0,2,
        20,1,0,0,0,4,23,1,0,0,0,6,27,1,0,0,0,8,31,1,0,0,0,10,42,1,0,0,0,
        12,46,1,0,0,0,14,54,1,0,0,0,16,17,3,2,1,0,17,18,3,14,7,0,18,19,5,
        0,0,1,19,1,1,0,0,0,20,21,3,4,2,0,21,22,3,6,3,0,22,3,1,0,0,0,23,24,
        5,1,0,0,24,25,5,2,0,0,25,26,3,8,4,0,26,5,1,0,0,0,27,28,5,3,0,0,28,
        29,5,2,0,0,29,30,3,8,4,0,30,7,1,0,0,0,31,32,5,4,0,0,32,37,3,10,5,
        0,33,34,5,5,0,0,34,36,3,10,5,0,35,33,1,0,0,0,36,39,1,0,0,0,37,35,
        1,0,0,0,37,38,1,0,0,0,38,40,1,0,0,0,39,37,1,0,0,0,40,41,5,6,0,0,
        41,9,1,0,0,0,42,43,5,4,0,0,43,44,3,12,6,0,44,45,5,6,0,0,45,11,1,
        0,0,0,46,51,5,10,0,0,47,48,5,5,0,0,48,50,5,10,0,0,49,47,1,0,0,0,
        50,53,1,0,0,0,51,49,1,0,0,0,51,52,1,0,0,0,52,13,1,0,0,0,53,51,1,
        0,0,0,54,55,5,7,0,0,55,56,5,8,0,0,56,57,5,1,0,0,57,58,5,5,0,0,58,
        59,5,3,0,0,59,60,5,9,0,0,60,15,1,0,0,0,2,37,51
    ]

class ProductoPuntoParser ( Parser ):

    grammarFileName = "ProductoPunto.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'matrizA'", "'='", "'matrizB'", "'['", 
                     "','", "']'", "'producto'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "NUM", "WS" ]

    RULE_program = 0
    RULE_declaracionMatrices = 1
    RULE_matrizA = 2
    RULE_matrizB = 3
    RULE_listaFilas = 4
    RULE_fila = 5
    RULE_listaNum = 6
    RULE_operacion = 7

    ruleNames =  [ "program", "declaracionMatrices", "matrizA", "matrizB", 
                   "listaFilas", "fila", "listaNum", "operacion" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    NUM=10
    WS=11

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def declaracionMatrices(self):
            return self.getTypedRuleContext(ProductoPuntoParser.DeclaracionMatricesContext,0)


        def operacion(self):
            return self.getTypedRuleContext(ProductoPuntoParser.OperacionContext,0)


        def EOF(self):
            return self.getToken(ProductoPuntoParser.EOF, 0)

        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)




    def program(self):

        localctx = ProductoPuntoParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.declaracionMatrices()
            self.state = 17
            self.operacion()
            self.state = 18
            self.match(ProductoPuntoParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionMatricesContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def matrizA(self):
            return self.getTypedRuleContext(ProductoPuntoParser.MatrizAContext,0)


        def matrizB(self):
            return self.getTypedRuleContext(ProductoPuntoParser.MatrizBContext,0)


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_declaracionMatrices

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracionMatrices" ):
                listener.enterDeclaracionMatrices(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracionMatrices" ):
                listener.exitDeclaracionMatrices(self)




    def declaracionMatrices(self):

        localctx = ProductoPuntoParser.DeclaracionMatricesContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracionMatrices)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self.matrizA()
            self.state = 21
            self.matrizB()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizAContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaFilas(self):
            return self.getTypedRuleContext(ProductoPuntoParser.ListaFilasContext,0)


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_matrizA

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizA" ):
                listener.enterMatrizA(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizA" ):
                listener.exitMatrizA(self)




    def matrizA(self):

        localctx = ProductoPuntoParser.MatrizAContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_matrizA)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self.match(ProductoPuntoParser.T__0)
            self.state = 24
            self.match(ProductoPuntoParser.T__1)
            self.state = 25
            self.listaFilas()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizBContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaFilas(self):
            return self.getTypedRuleContext(ProductoPuntoParser.ListaFilasContext,0)


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_matrizB

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatrizB" ):
                listener.enterMatrizB(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatrizB" ):
                listener.exitMatrizB(self)




    def matrizB(self):

        localctx = ProductoPuntoParser.MatrizBContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_matrizB)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self.match(ProductoPuntoParser.T__2)
            self.state = 28
            self.match(ProductoPuntoParser.T__1)
            self.state = 29
            self.listaFilas()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaFilasContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def fila(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ProductoPuntoParser.FilaContext)
            else:
                return self.getTypedRuleContext(ProductoPuntoParser.FilaContext,i)


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_listaFilas

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaFilas" ):
                listener.enterListaFilas(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaFilas" ):
                listener.exitListaFilas(self)




    def listaFilas(self):

        localctx = ProductoPuntoParser.ListaFilasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_listaFilas)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(ProductoPuntoParser.T__3)
            self.state = 32
            self.fila()
            self.state = 37
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 33
                self.match(ProductoPuntoParser.T__4)
                self.state = 34
                self.fila()
                self.state = 39
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 40
            self.match(ProductoPuntoParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FilaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def listaNum(self):
            return self.getTypedRuleContext(ProductoPuntoParser.ListaNumContext,0)


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_fila

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFila" ):
                listener.enterFila(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFila" ):
                listener.exitFila(self)




    def fila(self):

        localctx = ProductoPuntoParser.FilaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_fila)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(ProductoPuntoParser.T__3)
            self.state = 43
            self.listaNum()
            self.state = 44
            self.match(ProductoPuntoParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaNumContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUM(self, i:int=None):
            if i is None:
                return self.getTokens(ProductoPuntoParser.NUM)
            else:
                return self.getToken(ProductoPuntoParser.NUM, i)

        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_listaNum

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterListaNum" ):
                listener.enterListaNum(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitListaNum" ):
                listener.exitListaNum(self)




    def listaNum(self):

        localctx = ProductoPuntoParser.ListaNumContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_listaNum)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(ProductoPuntoParser.NUM)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 47
                self.match(ProductoPuntoParser.T__4)
                self.state = 48
                self.match(ProductoPuntoParser.NUM)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return ProductoPuntoParser.RULE_operacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperacion" ):
                listener.enterOperacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperacion" ):
                listener.exitOperacion(self)




    def operacion(self):

        localctx = ProductoPuntoParser.OperacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_operacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 54
            self.match(ProductoPuntoParser.T__6)
            self.state = 55
            self.match(ProductoPuntoParser.T__7)
            self.state = 56
            self.match(ProductoPuntoParser.T__0)
            self.state = 57
            self.match(ProductoPuntoParser.T__4)
            self.state = 58
            self.match(ProductoPuntoParser.T__2)
            self.state = 59
            self.match(ProductoPuntoParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





