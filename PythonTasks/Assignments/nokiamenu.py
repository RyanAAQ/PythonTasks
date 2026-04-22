print("List of menu functions \n1.  Phone book\n2.  Messages\n3.  Chat\n4.  Call register\n5.  Tones\n6.  Settings\n7.  Call divert\n8.  Games\n9.  Calculator\n10. Reminders\n11. Clock\n12. Profiles\n13. SIM services.\n0. Power off")

running = 1
while running > 0:
    main_menu_choice = int(input("Select\n"))
    match main_menu_choice:
        case(1):
            phone_book_running = 1
            while phone_book_running > 0:
                print("Phone book\n1. Search\n2. Service Nos\n3. Add name\n4. Erase\n5. Edit\n6. Assign Tone\n7. Send b'card\n8. Options\n9. Speed dials\n10. Voice tags\n0. Return")
                phone_book_choice = int(input("Select\n"))
                match phone_book_choice:
                    case 1:
                        print("Search")
                    case 2:
                        print("Service Nos")
                    case 3:
                        print("Add name")
                    case 4:
                        print("Erase")
                    case 5:
                        print("Edit")
                    case 6:
                        print("Assign Tone")
                    case 7:
                        print("Send b'card")
                    case 8:
                        print("Options\n1. Type of view\n2. Memory status")
                        options_choice = int(input("Select\n"))
                        match options_choice:
                                case 1:
                                    print("Type of view")
                                case 2:
                                    print("Memory status")
                    case 9:
                        print("Speed dials")
                    case 10:
                        print("Voice tags")
                    case 0:
                        print("Turning off")
                        phone_book_running = 0

        case 2:
            messages_running = 1
            while messages_running > 0:
                print("Messages\n1. Write messages\n2. Inbox\n3. Outbox\n4. Picture messages\n5. Templates\n6. Smileys\n7. Message settings\n8. Info service\n9. Voice mailbox number\n10. Service command editor")
                messages_choice = int(input("Select\n"))
                match messages_choice:
                    case 1:
                        print("Write messages")
                    case 2:
                        print("Inbox")
                    case 3:
                        print("Outbox")
                    case 4:
                        print("Picture messages")
                    case 5:
                        print("Templates")
                    case 6:
                        print("Smileys")
                    case 7:
                        message_settings_running = 1
                        while message_settings_running > 0:
                            print("Message settings\n1. Set\n2. Common")
                            message_settings_choice = int(input("Select\n"))
                            match message_settings_choice:
                                case 1:
                                    print("Set\n1. Message center number\n2. Message sent as\n3. Message validity")
                                    set_choice = int(input("Select\n"))
                                    match set_choice:
                                        case 1:
                                            print("Message center number")
                                        case 2:
                                            print("Message sent as")
                                        case 3:
                                            print("Message validity")
                                case 2:
                                    print("Common\n1. Delivery reports\n2. Reply via same center\n3. Character support")
                                    common_choice = int(input("Select\n"))
                                    match common_choice:
                                        case 1:
                                            print("Delivery reports")
                                        case 2:
                                            print("Reply via same center")
                                        case 3:
                                            print("Character support")
                                case 0:
                                    message_settings_running = 0
                    case 8:
                        print("Info service")
                    case 9:
                        print("Voice mailbox number")
                    case 10:
                        print("Service command editor")
                    case 0:
                        print("Returning")
                        messages_running = 0

        case 3:
            print("Chat")

        case 4:
            call_register_running = 1
            while call_register_running > 0:
                print("Call register\n1. Missed calls\n2. Received calls\n3. Dialled numbers\n4. Erase recent call list\n5. Show call duration\n6. Show call costs\n7. Call cost settings\n8. Prepaid credit\n0. Return")
                call_register = int(input("Select\n"))
                match call_register:
                    case 1:
                        print("Missed calls")
                    case 2:
                        print("Received calls")
                    case 3:
                        print("Dialled numbers")
                    case 4:
                        print("Erase recent call list")
                    case 5:
                        print("Show call duration\n1. Last call duration\n2. All calls duration\n3. Received calls duration\n4. Dialled calls duration\n5. Clear timers\n0. Return")
                        call_duration_choice = int(input("Select\n"))
                        match call_duration_choice:
                            case 1:
                                print("Last call duration")
                            case 2:
                                print("All calls duration")
                            case 3:
                                print("Received calls duration")
                            case 4:
                                print("Dialled calls duration")
                            case 5:
                                print("Clear timers")
                    case 6:
                        print("Show call costs")
                    case 7:
                        print("Call cost settings")
                    case 8:
                        print("Prepaid credit")
                    case 0:
                        call_register_running = 0

        case 5:
            print("Tones opening...")
        case 6:
            print("Settings opening...")
        case 7:
            print("Call divert opening...")
        case 8:
            print("Games opening...")
        case 9:
            print("Calculator opening...")
        case 10:
            print("Reminders opening...")
        case 11:
            print("Clock opening...")
        case 12:
            print("Profiles opening...")
        case 13:
            print("SIM services opening...")
        case 0:
            print("Returning")
            running = 0

