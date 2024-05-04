# hindi_alphabet = 'अ आ इ ई उ ऊ ऋ ऌ ऍ ए ऐ ऑ ऒ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह ळ क्ष ज्ञ'
# gujarati_alphabet = 'અ આ ઇ ઈ ઉ ઊ ઋ ઌ ઍ એ ઐ ઑ ઒ ઓ ઔ ક ખ ગ ઘ ઙ ચ છ જ ઝ ઞ ટ ઠ ડ ઢ ણ ત થ દ ધ ન પ ફ બ ભ મ ય ર લ વ શ ષ સ હ ળ ક્ષ જ્ઞ'
# english_alphabet = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'
# japanese_alphabet = 'ア イ ウ エ オ カ キ ク ケ コ サ シ ス セ ソ タ チ ツ テ ト ナ ニ ヌ ネ ノ ハ ヒ フ ヘ ホ マ ミ ム メ モ ヤ ユ ヨ ラ リ ル レ ロ ワ ヰ ヱ ヲ ン'
# marathi_alphabet = 'अ आ इ ई उ ऊ ऋ ऌ ऍ ए ऐ ऑ ऒ ओ औ क ख ग घ ङ च छ ज झ ञ ट ठ ड ढ ण त थ द ध न प फ ब भ म य र ल व श ष स ह ळ क्ष ज्ञ'
# punjabi_alphabet = 'ਅ ਆ ਇ ਈ ਉ ਊ ਏ ਐ ਓ ਔ ਕ ਖ ਗ ਘ ਙ ਚ ਛ ਜ ਝ ਞ ਟ ਠ ਡ ਢ ਣ ਤ ਥ ਦ ਧ ਨ ਪ ਫ ਬ ਭ ਮ ਯ ਰ ਲ ਵ ਸ਼ ਸ਼ ਸ ਹ ਲ਼ ਕ੍ਸ਼ ਜ੍ਞ'

# alphabets = list(hindi_alphabet + ' ' + gujarati_alphabet + ' ' + english_alphabet + ' ' + japanese_alphabet + ' ' + marathi_alphabet + ' ' + punjabi_alphabet)

# print(type(alphabets))
# for x in alphabets:
#     if x == ' ':
#         alphabets.remove(x)
#     else:
#         pass

# print(alphabets)


# import pandas as pd

# # Load the first CSV file
# df1 = pd.read_csv('True.csv')

# # Load the second CSV file
# df2 = pd.read_csv('Fake.csv')

# # Concatenate the two DataFrames
# concatenated_df = pd.concat([df1, df2], ignore_index=True)

# # Save the concatenated DataFrame to a new CSV file
# concatenated_df.to_csv('concatenated_file.csv', index=False)






import pandas as pd

# Specify the path to your Excel file
excel_file_path = 'main-1.xlsx'

# Read the Excel file
df = pd.read_excel(excel_file_path)

# Specify the path to the output CSV file
csv_file_path = 'testing_dataset.csv'

# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"Excel file has been converted to CSV and saved as {csv_file_path}")
