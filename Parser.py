from pyparsing import *

if_condition = (
    Suppress(Literal("[")) +
    Word(printables).setResultsName("subject") +
    Word(alphanums).setResultsName("verb") +
    Optional(
        Word(alphanums).setResultsName("object")
    ) +
    Suppress(Literal("]"))
)

else_condition = (
    Suppress(Literal("[else]"))
)

condition_text = (
    SkipTo(Literal("[") | Literal("}")).setParseAction(lambda t: t[0].strip())
)

condition_block = Group(
    Suppress(Literal("{")) +
    Group(
        if_condition.setResultsName("condition") +
        condition_text.setResultsName("condition_text")
    ).setResultsName("if_condition") +
    Group(
        Optional(
            else_condition +
            condition_text.setResultsName("condition_text")
        )
    ).setResultsName("else_condition") +
    Suppress(Literal("}"))
)

desc_block = (
    OneOrMore(
        condition_block |
        Word(printables)
    )
)

# roomID = Suppress(Literal("+")) + Word(alphanums) + Suppress(Literal(":"))
# textBlock = ZeroOrMore()

"""
TODO: need parsed condition block to be tuple where first item is key (but not
dictionary because can have duplicates). For the moment, since there currently
arent any other description-based entities beside conditional blocks.
"""

# print(desc_block.parseString("sfdlk  jklf jdksl fds {[dfsj f] djfd sds [else] slkd sd dsfaf ksd } hi"))
