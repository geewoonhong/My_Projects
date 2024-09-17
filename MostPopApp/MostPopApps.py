from csv import reader

try:
    #Google
    with open('D:/Programming/python/My_Projects/MostPopApp/data/googleplaystore.csv', 'r', encoding='utf-8') as opened_file:
        read_file = reader(opened_file)
        android = list(read_file)
        android_header = android[0]
        android = android[1:]

    # Apple
    with open('D:/Programming/python/My_Projects/MostPopApp/data/AppleStore.csv', 'r', encoding='utf-8') as opened_file:
        read_file = reader(opened_file)
        ios = list(read_file)
        ios_header = ios[0]
        ios = ios[1:]

except FileNotFoundError as e:
    print(e)
except UnicodeDecodeError as e:
    print("Encoding error:", e)

def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n')
    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print("Number of columns:", len(dataset[0]))

def check_data_row_len(dataset, header):
    head_row = header
    data = dataset
    for index, row in enumerate(dataset):
        if len(row) != len(head_row):
            print(index)
            print(row)
            print("Number of columns:", len(row))
            del data[index]
            print("Deleted Error")

class CleanData:
    def __init__(self):
        self.dups = []
        self.unique = []
        self.android_clean = []
        self.ios_clean = []

    def check_for_dups(self, dataset):
        if dataset is android:
            self.dups = []
            self.unique = []
            for app in android:
                name = app[0]
                if name in self.unique:
                    self.dups.append(name)
                else:
                    self.unique.append(name)
        elif dataset is ios:
            self.dups = []
            self.unique = []
            for track_name in ios:
                name = track_name[0]
                if name in self.unique:
                    self.dups.append(name)
                else:
                    self.unique.append(name)

#I have a dict of the app name and its highest num of user/reviews
    def remove(self, dataset):
        review_max = {}
        already_added = []
        for app in android:
            name = app[0]
            n_reviews = float(app[3])
            if name in review_max and review_max[name] < n_reviews:
                review_max[name] = n_reviews
            elif name not in review_max:
                review_max[name] = n_reviews
        for app in android:
            name = app[0]
            num_reviews = float(app[3])
            if name not in already_added and num_reviews == review_max[name]:
                self.android_clean.append(app)
                already_added.append(name)

    def is_eng(self, string):
        flag = 0
        for character in string:
            if ord(character) < 0 or ord(character)>127:
                flag += 1
        if flag > 3:
            return False
        return True

    def remove_non_eng_android(self):
        data = self.android_clean
        cleaned = []
        for app in data:
            name = app[0]
            if self.is_eng(name):
                cleaned.append(app)
            self.android_clean = cleaned

    def remove_non_eng_ios(self, dataset):
        data = dataset
        cleaned = []
        for app in data:
            name = app[1]
            if self.is_eng(name):
                cleaned.append(app)
            self.ios_clean = cleaned

    def remove_non_free_android(self):
        data = self.android_clean
        cleaned = []
        for app in data:
            price = app[7]
            if price == '0':
                cleaned.append(app)
            self.android_clean = cleaned

    def remove_non_free_ios(self):
        data = self.ios_clean
        cleaned = []
        for app in data:
            price = app[4]
            if price == '0.0':
                cleaned.append(app)
            self.ios_clean = cleaned

    def explore_clean_android(self):
        dataset = self.android_clean
#         for row in dataset:
#             print(row)
#             print('\n')
        print('Number of rows:', len(dataset))

    def explore_clean_ios(self):
        dataset = self.ios_clean
        #         for row in dataset:
        #             print(row)
        #             print('\n')
        print('Number of rows:', len(dataset))







print("Android data")
print(android_header)
print('\n')
print("Row length discrepancies: ")
check_data_row_len(android, android_header)
print('\n')
print("Check for Dups ")
clean = CleanData()
clean.check_for_dups(android)
print('Num of Dups:', len(clean.dups))
print('\n')
print("Remove Dups")
clean.remove(android)
print("Checking if dups were properly removed:")
clean.explore_clean_android()
print('\n')
print("Check for non-English apps ")
clean.remove_non_eng_android()
print("Checking if non eng were properly removed:")
clean.explore_clean_android()
print('\n')
print("Check for Free apps ")
clean.remove_non_free_android()
print("Checking if non free apps were properly removed:")
clean.explore_clean_android()
cleaned_android = clean.android_clean


print('\n')
print("IOS data")
print(ios_header)
print('\n')
print("Row length discrepancies: ")
check_data_row_len(ios, ios_header)
clean.check_for_dups(ios)
print('Num of Dups:', len(clean.dups))
print('\n')
print("Check for non-English apps ")
clean.remove_non_eng_ios(ios)
print("Checking if non eng were properly removed:")
clean.explore_clean_ios()
print('\n')
print("Check for Free apps ")
clean.remove_non_free_ios()
print("Checking if non free apps were properly removed:")
clean.explore_clean_ios()
cleaned_ios = clean.ios_clean
print('\n')
print('\n')
explore_data(cleaned_android, 0, 3, False)
explore_data(cleaned_ios, 0, 3, False)


def freq_table(dataset, index):
    table = {}
    total = 0
#check the value you're interested in. Then count how many times
#this category appears. Store this as the key
    for row in dataset:
        key = row[index]
        total += 1
        if key in table:
            table[key] += 1
        else:
            table[key] = 1
# for each key the value will be the percentage of how often that key appears
    table_percent = {}
    for key in table:
        percent = (table[key] / total) * 100
        table_percent[key] = percent
    return table_percent

def display_table(dataset, index):
    table = freq_table(dataset, index)
    table_display = []
    for key in table:
        key_val_as_tuple = (table[key], key)
        table_display.append(key_val_as_tuple)

    table_sorted = sorted(table_display, reverse = True)
    for entry in table_sorted:
        print(entry[1], ':', entry[0])


display_table(cleaned_ios, -5)
print('\n')
display_table(cleaned_android, 1)

#avg number of installs for each genre
print('\n')
genres_ios = freq_table(cleaned_ios, -5)
for genre in genres_ios:
    total = 0
    len_genre = 0
    for app in cleaned_ios:
        genre_app = app[-5]
        if genre_app == genre:
            n_ratings = float(app[5])
            total += n_ratings
            len_genre += 1
    avg_n_ratings = total / len_genre
    print(genre, ':', avg_n_ratings)
print('\n')

#avg number of installs for each genre
categories_android = freq_table(cleaned_android, 1)
for category in categories_android:
    total = 0
    len_category = 0
    for app in cleaned_android:
        category_app = app[1]
        if category_app == category:
            n_installs = app[5]
            n_installs = n_installs.replace(',', '')
            n_installs = n_installs.replace('+', '')
            total += float(n_installs)
            len_category += 1
    avg_n_installs = total / len_category
    print(category, ':', avg_n_installs)
