import math
from datetime import datetime

# TEXT = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Euismod quis aute option nihil nonumy option, hendrerit tempor accumsan deserunt tation tempor adipisici cupiditat invidunt. Iure facilisi est augue assum, tation eos stet adipiscing zzril nostrud labore facer voluptua delenit laborum sea wisi. Volutpat praesent velit consequat sadipscing cupiditat. Reprehenderit laboris velit."
#
# # text = input("Enter text for analyze: ")
#
# print(f"Analyze texts: {TEXT}")
#
# words = TEXT.split(" ")
# sentences = TEXT.split(". ")
#
# print(words)
# print(sentences)
#
# count_sentence = len(sentences)
# word_count = len(words)
#
# if count_sentence > 0:
#     avg_words_sent = word_count / count_sentence
# else:
#     avg_words_sent = 0
#
# print(f"Number of sentences: {count_sentence}")
# print(f"Number of words: {word_count}")
# print(f"Average number of words in a sentence: {math.ceil(avg_words_sent)}")


initial_price = 2000000  # грн

year_of_manufacture = int(input("Enter the year of manufacture of the vehicle: "))
current_mileage = int(input("Enter the mileage of the car (in km): "))

current_year = datetime.now().year

age_of_car = current_year - year_of_manufacture
depreciation = age_of_car * 0.1
final_price = initial_price * (1 - depreciation)

if age_of_car > 0:  # Уникнення ділення на нуль
    average_annual_mileage = current_mileage / age_of_car
else:
    average_annual_mileage = current_mileage

print(f"""
Information about the car:
- Year of release: {year_of_manufacture}
- Age of the vehicle: {age_of_car} years
- Initial cost: {initial_price} UAH
- Vehicle mileage: {current_mileage} km
- Average annual mileage: {average_annual_mileage:.0f} km/year
- Approximate current value: {final_price:.2f} UAH
""")