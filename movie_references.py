# movie_references.py

# TODO: catch error if entry is missing (e.g. Director)

# import os for using its functions on file names
import os

# import pandas for using its data frame
import pandas as pd

test = "AUS"      # test:= "EIN" oder "AUS" ("EIN": mit Zusatz-Infos in out_datei)
sep = ";"         # separator
nl = "\n"         # new line (i.e. symbol for end of line)

# name of our input file
movie_datei = "Unsere_Datei_movieID_serial.csv"

# name of our output file
# it is the concatenation of the name of our input file without the extension ('.csv')
# and the new extension '_ref.csv'
# concretely: 'Unsere_Datei_movieID_serial' + '_ref.csv' = 'Unsere_Datei_movieID_serial_ref.csv'
out_datei = os.path.splitext(movie_datei)[0] + '_ref.csv'

# build the header line (first line)
out_header = "Source;Target\n"

# open the output file in write (exactly: overwrite) modus
csv_out = open(out_datei, "w")
# write the header line into the out_datei
csv_out.write(out_header)

# function to write the out_datei
def write_record(ind_target):
  target = df['movieId'][ind_target]               # get target movieId  
  netto = str(row_movieId) + sep + str(target)     # row_movieId:= source
  if row_movieId == target:                        # reflexiv
    return
  if test.upper() == "EIN":
    # provide additional info
    title =  df['Title'][ind_target]
    genre =  df['Genre'][ind_target]   
    director = df['Director'][ind_target]
    brutto = netto + "    # Target: [" + title + ", " + genre + ", " + director + "]"
  else:
    brutto = netto
  csv_out.write(brutto + nl)
  

# HEAD: movieId,Title,Genre,Director
df = pd.read_csv(movie_datei, sep = ',') # read csv-file into data frame
for ind in df.index:                     # Iterating over rows using index (movieId)
  row_movieId = df['movieId'][ind]
  row_genre = df['Genre'][ind]
  row_director = df['Director'][ind]
  # get all lines having the same Genre as that in variable 'row_genre'
  target_genre = df.query('Genre == ' + "\"" + row_genre + "\"")
  for item in target_genre.index:     # for all found genres:
    write_record(item)                # write record (line) to out_datei
  # get all lines having the same Director as that in variable 'row_director'
  target_director = df.query('Director == ' + "\"" + row_director + "\"")
  for item in target_director.index:  # for all found directors:
    write_record(item)                # write record (line) to out_datei
csv_out.close()                       # write buffer to file and close the file
