@bot.event
async def on_message(message):
    msg = message.content

    with open("discordbots\.words.json", "r+") as file:
        words_json = json.load(file)
        file.close()
        #this opens the json file and loads it

    bad_words = words_json["bad_words"]
    #labels the file and it looks for the dictionary "bad_words"

    broken_up_msg = msg.split()
    print(broken_up_msg)
    #not sure what this is but i think it changes the incoming texts to lists

    for bad_word in bad_words:
        #looks for badwords in the json badwords
        if bad_word in broken_up_msg:
            channel = message.channel
            await message.delete()
            await channel.send("no swearing")
    #this waits for someone to send a word in the json dicitonary and it deletes it

@bot.event 
async def on_message(message):
        msg = message.content
        
        with open("discordbots\kyla.json", "r+") as file:
            kyla_json =  json.load(file)
            file.close()

        kyla_reactions = kyla_json["kiss"]

        broken_up_msg = msg.split()
        print(broken_up_msg)

        for kyla_reaction in kyla_reactions:
            if kyla_reaction in broken_up_msg:
                channel = message.channel
                await channel.send(":**")