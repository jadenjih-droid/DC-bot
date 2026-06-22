Main idea/brain storming
-You activate a command which shows a menu with a button saying "roll". Clicking this button will cause it to roll a random fruit in the pool of possible fruits. After this, you can either skip it or reroll it. Doing so will force you to hold onto said fruit and you can do two things. You can either sell it or roll it of for a new fruit. 
-You start with and apple no matter what and 0 dollars therefore, you must sell it and are unable to reroll it.
When selling a a fruit it will have a fixed value. The value can be changed after the basis of he command is finished.
-Well known fruits will be more common ex:(apple or orange) while fruits that are less known will be more rare and worth more (mango, Durian, or Rambutan)


Mechanics tba:
    -Weight system
    -Auction 
    -Vegetables

Basis of the code itself/core mechanic:
    -When using the command, it would spawn a card that shows an image of a RANDOM fruit.
    -When it is is your first time using the command it will be an apple NO MATTER WHAT.
    -You will then have two options to either sell the fruit or reroll it.
    -There will be a seprate menu if you use the command /shop to buy upgrads. Upgrades profit gain, luck anything in a srand rng game.
    -
    

Data structure:
    Define fruits={
        "apple": [price:10, weight:60],
        "mango": [price:30, weight:180],
        "orange" [price:5, weight:30],
        "blueberry" [price:2.5, weight:15],
        "watermelon" [price:50, weight:300],
        "honeydew" [price:45, weight:270],
        "lychee" [price:90, weight:20],
        "cherry" [price:50, weight:30],
        "strawberry" [price:5, weight:20],
        "blackberry" [price:5, weight:10],
        "banana" [price:15, weight:40],
        "tomato" [price:5000, weight:10],
        "pineapple" [price:40, weight:50],
    }

    Define user_profile={
        balance=0
        holding_fruit=none
        is_first_time: True,
        upgrades: {profit_multiplier: 1.0, luck_bonuses:0}
    }
    // DB of all user(Key:user_ID, Value: UserProfile)
    Define USER_DATABASE={}

/game
    Function ON_COMMAND_GAME(User):
        // 1.define new user and/or register
        if User.ID not in USER_DATABASE Then:
            USER_DATABASE[User.ID]=Create New UserProfile

        Currenct_User=USER_DATABASE[User.ID]
        //2. UI button activation from the status of"now"
            Function UPDATE_BUTTON_STATES():
                If Current_User.holding_fruit is None THen
                Enable BUTTON_ROLL
                Disable BUTTON_SELL
                Disable BUTTON_REROLL
            Else:
            DIsable BUTTON_ROLL
            Enable BUTTON_SELL

            // reroll price(ex: 10$), reroll only when its not first time/roll(apple)
                If Current_User.balance>=10 AND
            Current_User.is_first_time==False Then:
                Enable BUTTON_REROLL
            Else:
                Disable BUTTON_REROLL

        //3. game menu msg(deafault setting for button)
            UPDATE_BUTTONS_STATES()
            Display EmbedMessage(balance, frut info)with Buttons[Roll, Sell, Reroll]


    Function ON_CLICK_ROLL(User):
        Current_User=USER_DATABASE[User.ID]

        //first time always get apple
        if current_User.is_First_time==True Then:
            Current_User.holding_fruit="Apple"
            Current_User.is_first_time=False//random after first time

        //Weighted random selection from the second pick
        Else:
            Current_User.holding_fruit=
        RANDOM_CHOOSE_WEIGHT(FRUIT_POOL)

            //Update button states(Determine whether to disable Roll and enable Sell/Reroll)
                UPDATE_BUTTON_STATES()

                Update EmbedMessage(Display selected fruit image and information, update button UI)

                Function On_CLICK_Sell(User):
                Current_User==USER_DATABASE[User.ID]
                Fruit_Name=Current_User.holding_fruit

                //Calculate base prince and apply upgrade multiplier
                Base_Price=FRUIT_POOL[Fruit_Name].Price
                Final_Profit=Base_Price*
            Current_User.upgrades.profit_multiplier

                //Settlement
                Current_User.balance+=Final_profit
                Current_User.holding_fruit=None//Clear inventory

                UPDATE_BUTTON_STATES()

                Update EmbedMessage(Display sale payout, display current balance, update button UI)
                Function ON_CLICK_REROLL(User):
                    Current_User=USER_DAtABASE[User.ID]
                    Reroll_Cost=10

                    //Balance verification(Security and error preventation)
                    if Current_User.balance<Reroll_cost Then:
                        Show Error("insufficent Balance.")
                        Exit Function

                    //Deduct cost and instantly reroll new fruit
                    CUrrent_User.balance-=Reroll_Cost
                    Current_User.Holding_fruit=
                RANDOM_CHOOSE_BY_WEIGHT(FRUIT_POOL)

                    UPDATE_BUTTON_STATES()

                    Update EmbedMessage(Display reroll result, display deducted
                balance, update button UI)
