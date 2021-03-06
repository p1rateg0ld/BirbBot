# store lists of recognized input and other lists birbBot checks but doesn't say (mostly)

import voiceLines
import ServerInfo

birbBotNames = [
    "birbbot",
    "birb bot",
    "birb_bot",
    "<@511403822418231296>"
    ]


rosters = {
    # random characters to prevent it from being used by other users
    "__default__": ""  # will store the default roster used in !join

}
voices = {
    "agathaarcher": voiceLines.AgathaArcher(),
    "agathamaa": voiceLines.AgathaManAtArms(),
    "agathavan": voiceLines.AgathaVanguard(),
    "agathavanguard": voiceLines.AgathaVanguard(),
    "agathaknight": voiceLines.AgathaKnight(),
    "masonarcher": voiceLines.MasonArcher(),
    "masonmaa": voiceLines.MasonManAtArms(),
    "masonvan": voiceLines.MasonVanguard(),
    "masonvanguard": voiceLines.MasonVanguard(),
    "masonknight": voiceLines.MasonKnight(),
    "unused": voiceLines.UnusedVoice(),
}


feintLines = [
    "feinted me",
    "i was feinted",
    "feints suck",
    "fuck feints",
    "feints are bullshit",
    "feints are fucking bullshit",
    "don't like feints",
    "hate feints",
    "feints are an exploit",
    "feint me"
    ]

# names birb bot is not allowed to say
forbiddenNames = [
    "hitler",
    "adolf",
    "adolf hitler",
    "adolfhitler",
    "stalin",
    "joseph stalin",
    "josephstalin",
    "pol pot",
    "polpot",
    "mao",
    "ben shapiro",
    "benshapiro",
    "donald trump",
    "trump",
    "donaldtrump",
    "realdonaldtrump",
    "jordan peterson",
    "jordanpeterston",
    "jordan_peterson"
]


specialResponseNames = {
    "birbbot": {"taunt": voiceLines.BirbBotSnark(),
                "respect": "Thank you, {0.author.mention} :hearts:",
                "thank": "You are very welcome, {0.author.mention} :hugging:"
                },
    "birb bot": {"taunt": voiceLines.BirbBotSnark(),
                 "respect": "Thank you, {0.author.mention} :hearts:",
                 "thank": "You are very welcome, {0.author.mention} :hugging:"
                 },
    "birb_bot": {"taunt": voiceLines.BirbBotSnark(),
                 "respect": "Thank you, {0.author.mention} :hearts:",
                 "thank": "You are very welcome, {0.author.mention} :hugging:"
                 },
    "<@511403822418231296>": {"taunt": voiceLines.BirbBotSnark(),
                              "respect": "Thank you, {0.author.mention} :hearts:",
                              "thank": "You are very welcome, {0.author.mention} :hugging:"},
    "women": {"taunt": "You're trash, {0.author.mention}, learn some respect.",
              "respect": "https://www.youtube.com/watch?v=dfr4PrFxm0s",
              "thank": "https://www.youtube.com/watch?v=dfr4PrFxm0s"
              },
    "@everyone": {"taunt": "What if instead, everyone taunts you for thinking something this simple would work, {0.author.mention}?",
                  "respect": "We appreciate the sentiment, but this might not be the best way to show it, {0.author.mention}",
                  "thank": "You could better show your thankfulness by writing us each personal thank you letters, don't you think, {0.author.mention}?"
                  },
    "@here": {"taunt": "What if instead everyone taunts you for thinking something this simple would work, {0.author.mention}?",
              "respect": "We appreciate the sentiment, but this might not be the best way to show it, {0.author.mention}",
              "thank": "You could better show your thankfulness by writing us each personal thank you letters, don't you think, {0.author.mention}?"
              }
}


selfResponseDict = {
    "taunt": "Are you feeling okay, {0.author.mention}?",
    "thank": "Don't flatter yourself, {0.author.mention}",
    "respect": "I would, but the chat is too full of your ego for me to send a message right now, {0.author.mention}",
    "forbiddenName": "No"
}


voiceLineCommands = [
    "taunt",
    "respect",
    "thank"
]

recognizedServers = {
    "bigChiv": ServerInfo.ServerInfo("query.aspx?id=24", "Moorland Skirmishers | Gracious Welcome"),
    "smallChiv": ServerInfo.ServerInfo("query.aspx?id=25", "Moorland Skirmishers | Map Testing"),
    "bigMord": ServerInfo.ServerInfo("query.aspx?id=28", "Moorland Skirmishers ❊ Gracious Welcome"),
    "smallMord": ServerInfo.ServerInfo("query.aspx?id=33", "Moorland Skirmishers ❊ Intimate Encounters")
}

allInfoCommands = [  # commands that will return all server info
    "ms"
]

checkForCommands = [  # commands that will activate the checkfor feature
    "checkfor",
]

messageCommands = {  # general one-response commands
    "goodnight": "Goodnight, {0.author.mention}",
    "scream": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA",
    "screm": ":screm:",
    "kiss": ":kissing_heart:",
    "arrest": ":police_car:",
    "f10": "I'm calling the police, {0.author.mention}",
    "c": "AAAARRRRRRRRRRRGGGGGGGGGGGGGGG",
    "quadfeint": "Sorry, this move is usable only by god himself",
    "sheildjump": "Reported for hacks",
    "z4": "KILL THOSE ARCHERS!",
    "help": "Documentation has been sent to you. If you did not receive it, please make your DM's public"
}

dmCommands = {  # commands that will result in a DM response
    "help": "__**BIRB BOT COMMAND DOCUMENTATION**__\n"
            "<> : signifies optional parameter\n"
            "[]: signifies required parameter\n"
            "__*Do not include brackets when entering command*__\n\n"

            "```Command                    | Result\n"
            "--------------------------------------------------------\n"
            "!hello                     | Say hello\n"
            "![server]                  | Return server info\n"
            "!ms                        | Return info from all Moorland Skirmishers servers\n"
            "!checkfor [name]           | Search for player or group\n"

            "!taunt <class> <name>      | Say a taunt line\n"
            "!respect <class> <name>    | Say a respect line\n"
            "!thank <class> <name>      | Say a thanks line ``` \n"

            "\n__**Server Names**__\n"
            "**64** : Main 64 slot Chivalry server\n"
            "**62** : Secondary 62 slot Chivalry server\n"

            "\n__**Class Names**__\n"
            "agathaMAA\n"
            "agathaArcher\n"
            "agathaVan\n"
            "agathaKnight\n"
            "masonMAA\n"
            "masonArcher\n"
            "masonVan\n"
            "masonKnight\n"

            "\n__**CheckFor Function [Names]**__\n"
            "admins   --->   states if there are any admins on the specified server\n"
            "skirmishers   --->   states if there are any Moorland Skirmishers on the specified server\n"
            "Baron   --->   states if Baron Von Moorland is on the specified server\n"
            "<name>   --->   any name you want to search. You do not need to enter the  •҉   symbol, but other special characters will need to be accounted for\n"

            "\n__**Notes**__\n"
            "Capitalization does not matter\n"
            "BirbBot has a large number of commands not listed in documentation, *most* of which are not triggered with \"![command]\". They will likely reveal themselves in time\n"
            "Report any bugs found to Raysparks\n"

            "\n__**Examples**__\n"
            "!ms \"Mooland Skirmishers: Gracious Welcome is playing aocffa-moor_p with a population... \""
            "!checkFor admins   --->   \"There are currently admins on Gracious Welcome!\"\n"
            "!taunt  --->   \"Your wife is a hobby horse!\"\n"
            "!thank Malric   --->   \"Malric, thank you brother!\"\n"
            "!respect agathaVan Baron Von Moorland    --->   \"Baron Von Moorland, I dare say you matched even my own skills\"\n\n"
            "Note: Roster commands have been depreciated at this time and will not function. Let Raysparks know if you want to see their return",

    "rosterhelp": "__**THESE COMMANDS HAVE BEEN DEPRECIATED DUE TO GENERAL BUGGINESS AND LACK OF USE**__\n\n"
                  "__**BIRB BOT ROSTER COMMAND DOCUMENTATION**__\n"
                  "<> : signifies optional parameter\n"
                  "[]: signifies required parameter\n"
                  "__*Do not include brackets when entering command*__\n\n"

                  "**__BASIC COMMANDS__**\n"
                  "```Command                          | Result\n"
                  "--------------------------------------------------------\n"
                  "!<rosterName> join               | Join the most recent roster. Specify name to join a specific roster\n"
                  "!<rosterName> leave              | Leave the most recent roster. Specify name to join a specific roster```\n\n"
                   
                  "**__CREATOR COMMANDS__**\n"
                  "```Command                       | Result\n"
                  "--------------------------------------------------------\n"
                  "!newRoster [size] [name]         | Create a new roster of the specified size with the specified name\n"
                  "![rosterName] show               | Display the specified roster\n"
                  "![rosterName] alert              | Alert all members of the specified roster\n"
                  "CREATOR-ONLY COMMANDS            | These commands cannot be used by anyone but the person who created the roster\n"
                  "![rosterName] setSlots [size]    | Change the roster size to the newly specified size\n"
                  "![rosterName] register [@][name] | Register a new member that is not yourself. An [@] must be provided for \"!alert\" to alert them\n"
                  "![rosterName] remove [@]||[name] | Remove a member that is not yourself. Name or [@] is accepted\n"
                  "![rosterName] delete             | Permanently delete the specified roster\n\n```"
    
                  "\n**Examples:**\n"
                  "!newRoster 5 exampleRoster   --->   creates a new roster named \"exampleRoster\" of size 5\n"
                  "!newRoster join   --->   join newRoster\n"
                  "!exampleRoster register Birb @birb#1234   --->   registers a new member named Birb with an @ of @birb#1234\n"
                  "!exampleRoster register Birb   --->   registers a new member named Birb that will not be alerted\n"
                  "!exampleRoster remove Birb   --->   removes Birb from the roster. Also works provided the @\n"
                  "!exampleRoster setSlots 10   --->   changes the roster size to 10 with 5 waiting list slots"
}

hiddenCommandDict = {  # commands that do not begin with "!"
    "come hither": "come hither",
    "good bot": "*happy birb noises*",
    "best bot": "*happy birb noises*",
    "fantastic bot": "*happy birb noises*",
    "amazing bot": "*happy birb noises*",
    "great bot": "*happy birb noises*",
    "what is malric": "a dude!",
    "goodnight birbbot": "goodnight, {0.author.mention}",
    "goodnight birb bot": "goodnight, {0.author.mention}",
    "goodnight birb_bot": "goodnight, {0.author.mention}",
    "goodnight <@511403822418231296>" : "goodnight, {0.author.mention}",
    "goodnight, birbbot": "goodnight, {0.author.mention}",
    "goodnight, birb bot": "goodnight, {0.author.mention}",
    "goodnight, birb_bot": "goodnight, {0.author.mention}",
    "goodnight, <@511403822418231296>" : "goodnight, {0.author.mention}",
    "i love you birbbot": "I love you too, {0.author.mention}",
    "i love you birb bot": "I love you too, {0.author.mention}",
    "i love you birb_bot": "I love you too, {0.author.mention}",
    "i love you <@511403822418231296>": "I love you too, {0.author.mention}",
    "i love you, birbbot": "I love you too, {0.author.mention}",
    "i love you, birb bot": "I love you too, {0.author.mention}",
    "i love you, birb_bot": "I love you too, {0.author.mention}",
    "i love you, <@511403822418231296>": "I love you too, {0.author.mention}"

}

multiResponseCommands = {  # commands that have more than one possible response
    "hello": voiceLines.Hello()
}

recognizedChannels = {
    "rules-of-engagement": "454804299596169236",
    "announcements": "517530205750034433",
    "gracious-welcome": "351239360475168768",
    "mordhau": "494183423502581761",
    "events": "494183498769367040",
    "agatha": "312000965765234691",
    "mason": "312000920722341894",
    "server-status": "517530437300518912",
    "moorland-castle": "524294151211319316",
    "common-ground": "269236791196909569",
    "other-games": "551991231333531670",
    "music": "458070110889050123",
    "memes": "494183581497819136",
    "smut-stuff-nsfw": "461067966285611008",

    "documentation": "512750458184531984",
    "public-bot-testing": "512786062150729728",
    "private-bot-testing": "511405757783212069",
    "private-birbbot-usage": "550481595421687810"
}