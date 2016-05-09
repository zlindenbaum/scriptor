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

desc_block = Group(
    OneOrMore(
        condition_block |
        Word(printables)
    )
)

local_variable = (
    Suppress(Literal(".")) +
    Word(alphanums).setParseAction(lambda t: "." + t[0])
)

room_variables = Group(
    Suppress(
        Literal("Variables:") +
        LineEnd()
    ) +
    OneOrMore(
        Group(
            local_variable +
            Suppress(Literal("="))+
            Word(alphanums) +
            Suppress(LineEnd())
        )
    )
).setResultsName("local_variables")

path = Group(
    Word(alphanums).setResultsName("target") +
    Suppress(Literal("->")) +
    Word(alphanums).setResultsName("destination")
)

command = Group(
    OneOrMore(Word(alphanums)).setParseAction(lambda t: " ".join(t)) +
    Suppress(
        Literal(":") +
        LineEnd()
    ) +
    Group(OneOrMore(
        Word(alphanums).setResultsName("function") +
        Group(OneOrMore(
            local_variable |
            path |
            Word(alphanums) +
            Suppress(LineEnd())
        )).setResultsName("parameters")
    )) +
    Suppress(OneOrMore(LineEnd()))
)

room_commands = Group(
    Suppress(
        Literal("Commands:") +
        LineEnd()
    ) +
    OneOrMore(command)
).setResultsName("commands")

room_ID = (
    Suppress(Literal("+")) +
    Word(alphanums).setResultsName("id") +
    Suppress(Literal(":")) +
    Suppress(OneOrMore(LineEnd()))
)
# room_name = Literal("Name:") + desc_block + Suppress(OneOrMore(LineEnd()))
room_name = (
    Suppress(Literal("Name:")) +
    SkipTo(LineEnd()).setParseAction(lambda t: desc_block.parseString(str(t[0])))
)

room_desc = (
    Suppress(Literal("Description:")) +
    SkipTo(LineEnd()).setParseAction(lambda t: desc_block.parseString(str(t[0]))[0])
).setResultsName("description")
# room_desc = Literal("Description:") + desc_block + Suppress(OneOrMore(LineEnd()))
# room_desc = Literal("Description:") + OneOrMore(Word(printables)) + Suppress(LineEnd())

room_paths = Group(
    Suppress(Literal("Paths:") + LineEnd()) +
    OneOrMore(
        path +
        Suppress(LineEnd())
    )
).setResultsName("paths")

room = Group(
    room_ID +
    room_name &
    room_desc &
    Optional(room_commands) &
    Optional(room_variables) &
    Optional(room_paths)
)

combined = OneOrMore(
    OneOrMore(
        room
    )
)

parsed = """
+room1:

Name: A Room
Description: sfdlk jklf jdksl fds {[dfsj f] djfd sds [else] slkd sd dsfaf ksd } hi

Commands:
    throw switch:
        enable .lights
        do something

    throw switch2:
        enable .lights
        do something

Variables:
    .lights = true
    .an = off

Paths:
    north -> house
    south -> room2
"""
# print(local_variable.parseString(".hi"))

# print(roomCommands.parseString(parsed))

print(combined.parseString(parsed)[0])

# roomDesc

"""
TODO: need parsed condition block to be tuple where first item is key (but not
dictionary because can have duplicates). For the moment, since there currently
arent any other description-based entities beside conditional blocks.
"""
# with open("testInput2") as raw:
    # parsed = parseFile(raw)

# parsed = desc_block.parseString("sfdlk jklf jdksl fds {[dfsj f] djfd sds [else] slkd sd dsfaf ksd } hi")

# print(parsed)

# print(desc_block.parseString("sfdlk jklf jdksl fds {[dfsj f] djfd sds [else] slkd sd dsfaf ksd } hi"))
# print(type(parsed.asList()[0]))
