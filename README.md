# vedabase-scraper
A Python 3 script to extract all verses, translations and purports from [A.C. Bhaktivedanta Swami Prabhupada's](https://en.wikipedia.org/wiki/A._C._Bhaktivedanta_Swami_Prabhupada) [Bhagavad Gita as it is](https://www.asitis.com/), [Srimad Bhagavatam](https://en.wikipedia.org/wiki/Bhagavata_Purana) and [Caitanya Caritamrta](https://en.wikipedia.org/wiki/Chaitanya_Charitamrita) from the [vedabase.io](http://vedabase.io/en) website

#### Usage

**Important:** The scraper requires [Python](https://www.python.org/downloads/) 3.8.3+ and [pip](https://pip.pypa.io/en/stable/installation/) v19.2.3+

Steps:

1. Get a copy of the code:

        git clone git@github.com:kodymoodley/vedabase-scraper.git
    
2. Change into the `vedabase-scraper/` directory.

3. Type `pip install -r requirements.txt`

4. To view help information on how to use the `vedabase-scraper.py` script, type: `python vedabase-scraper.py -h`

5. Example usage to scrape text only from the Bhagavad Gita on [vedabase.io](https://vedabase.io/en/): `python vedabase-scraper.py --extract bg`

#### Output format

The scraper script will output a .csv file with four columns: `id, sanskrit, english, purport`. `id` represents the specific verse in the book; `sanskrit` represents the sanskrit transliteration of the verse; `english` represents the English translation of the sanskrit; and `purport` represents the purport text explaining the verse in English as depicted in the book. See the `output/` directory for example files generated after running the script.

## License

Copyright (2022) Kody Moodley

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

