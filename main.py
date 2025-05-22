import time
from colorama import Fore

def processing_animation():
    for _ in range(3):
        print(Fore.YELLOW + ".", end="", flush=True)
        time.sleep(0.5)
from textblob import TextBlob
from colorama import Fore, Style

def handle_ai(name):
    print(Fore.BLUE + "\n🔍 Let’s find the perfect movie for you!\n")

    # Display genres
    print(Fore.GREEN + "Available Genres:")
    for idx, genre in enumerate(genres, 1):
        print(f"{Fore.CYAN}{idx}. {genre}")
    print()

    # Genre input
    while True:
        genre_input = input(Fore.YELLOW + "Enter genre number or name: ").strip()
        if genre_input.isdigit() and 1 <= int(genre_input) <= len(genres):
            genre = genres[int(genre_input)-1]
            break
        elif genre_input.title() in genres:
            genre = genre_input.title()
            break
        print(Fore.RED + "Invalid input. Try again.\n")

    # Mood input
    mood = input(Fore.YELLOW + "How do you feel today? (Describe your mood): ").strip()
    print(Fore.BLUE + "\nAnalyzing mood", end="", flush=True)
    processing_animation()
    polarity = TextBlob(mood).sentiment.polarity
    mood_desc = "positive 😊" if polarity > 0 else "negative 😞" if polarity < 0 else "neutral 😐"
    print(f"\n{Fore.GREEN}Your mood is {mood_desc} (Polarity: {polarity:.2f}).\n")

    # IMDb rating input
    while True:
        rating_input = input(Fore.YELLOW + "Enter minimum IMDB rating (7.6-9.3) or 'skip': ").strip()
        if rating_input.lower() == 'skip':
            rating = None
            break
        try:
            rating = float(rating_input)
            if 7.6 <= rating <= 9.3:
                break
            print(Fore.RED + "Rating out of range. Try again.\n")
        except ValueError:
            print(Fore.RED + "Invalid input. Try again.\n")

    # Recommendation step
    print(f"{Fore.BLUE}\nFinding movies for {name}", end="", flush=True)
    processing_animation()

    recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
    if isinstance(recs, str):
        print(Fore.RED + recs + "\n")
    else:
        display_recommendations(recs, name)

    # Ask for more
    while True:
        action = input(Fore.YELLOW + "\nWould you like more recommendations? (yes/no): ").strip().lower()
        if action == 'no':
            print(Fore.GREEN + f"\nEnjoy your movie picks, {name}! 🎬🍿\n")
            break
        elif action == 'yes':
            recs = recommend_movies(genre=genre, mood=mood, rating=rating, top_n=5)
            if isinstance(recs, str):
                print(Fore.RED + recs + "\n")
            else:
                display_recommendations(recs, name)
        else:
            print(Fore.RED + "Invalid choice. Try again.\n")
