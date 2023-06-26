reserved = {
    "CONSTANT",
    "DECLARE",
    "FOR",
    "TO",
    "NEXT",
    "TYPE",
    "ENDTYPE",
    "INPUT",
    "OUTPUT",
    "IF",
    "THEN",
    "ELSE",
    "ENDIF",
    "CASE",
    "OF",
    "OTHERWISE",
    "ENDCASE",
    "REPEAT",
    "UNTIL",
    "WHILE",
    "ENDWHILE",
    "PROCEDURE",
    "ENDPROCEDURE",
    "CALL",
    "FUNCTION",
    "ENDFUNCTION",
    "PRIVATE",
    "PUBLIC",
    "AND",
    "OR",
    "NOT",
    "NEW",
    "CLASS",
    "INHERITS",
    "ARRAY",
    "RETURNS",
    "RETURN"
}

tokens = (
    # 数据类型
    "INTEGER",
    "REAL",
    "CHAR",
    "STRING",
    "BOOLEAN",
    # 算数运算
    "PLUS",
    "MINUS",
    "MUL",
    "DIV",
    # 符号
    "LEFT_PAREN", # (
    "RIGHT_PAREN", # )
    "LEFT_SQUARE", # [
    "RIGHT_SQUARE", # ]
    "LEFT_BRACE", # {
    "RIGHT_BRACE", # }
    "COLON", # :
    "COMMA", # ,
    "DOT", # .
    "POINTER", # ^
    # 逻辑运算
    "LESS",
    "GREATER",
    "EQUAL",
    "LESS_EQUAL",
    "GREATER_EQUAL",
    "NOT_EQUAL",
    # 赋值
    "ASSIGN", # <-
    # Identifier
    "ID",
) + tuple(reserved)

# 匹配正则表达式
t_ASSIGN = r"<-"
t_PLUS = r"\+"
t_MINUS = r"\-"
t_MUL = r"\*"
t_DIV = r"/"
t_LEFT_PAREN = r"\("
t_RIGHT_PAREN = r"\)"
t_LEFT_SQUARE = r"\["
t_RIGHT_SQUARE = r"\]"
t_LEFT_BRACE = r"\{"
t_RIGHT_BRACE = r"\}"
t_COLON = r":"
t_COMMA = r","
t_DOT = r"\."
t_LESS = r"<"
t_GREATER = r">"
t_EQUAL = r"="
t_LESS_EQUAL = r"<="
t_GREATER_EQUAL = r">="
t_NOT_EQUAL = r"<>"
t_POINTER = r"\^"
# 忽视空格
t_ignore = r" \t"

# 规则行为
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    # 如果是关键字
    if t.value in reserved:
        t.type = t.value
    else:
        t.type = 'ID'
    return t

def t_BOOLEAN(t):
    r'TRUE|FALSE'
    t.value = bool(t.value)
    return t

def t_CHAR(t):
    r'\'[\s\S]\''
    t.value = str(t.value)
    return t

def t_STRING(t):
    r'\"[\s\S+]+\"'
    t.value = str(t.value)
    return t

def t_REAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# 意外处理
def t_error(t):
    print(f"Keyword not fount: `{t.value[0]}` at line {t.lineno}")
    t.lexer.skip(1)

def t_new_line(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

# 符号优先级
precedence = (
    # 加减乘除
    ("left", "PLUS", "MINUS"),
    ("left", "MUL", "DIV"),
    # 比较运算
    ("left", "LESS", "GREATER", "LESS_EQUAL", "GREATER_EQUAL", "EQUAL", "NOT_EQUAL"),
    # 逻辑运算
    ("left", "AND"),
    ("left", "OR"),
    ("left", "NOT"),
)
