{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7936e436",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "505e089c",
   "metadata": {},
   "outputs": [],
   "source": [
    "sets = pd.read_csv('sets.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "2fbbebb2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>001-1</td>\n",
       "      <td>Gears</td>\n",
       "      <td>1965</td>\n",
       "      <td>1</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0011-2</td>\n",
       "      <td>Town Mini-Figures</td>\n",
       "      <td>1978</td>\n",
       "      <td>84</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0011-3</td>\n",
       "      <td>Castle 2 for 1 Bonus Offer</td>\n",
       "      <td>1987</td>\n",
       "      <td>199</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0012-1</td>\n",
       "      <td>Space Mini-Figures</td>\n",
       "      <td>1979</td>\n",
       "      <td>143</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0013-1</td>\n",
       "      <td>Space Mini-Figures</td>\n",
       "      <td>1979</td>\n",
       "      <td>143</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  set_num                        name  year  theme_id  num_parts\n",
       "0   001-1                       Gears  1965         1         43\n",
       "1  0011-2           Town Mini-Figures  1978        84         12\n",
       "2  0011-3  Castle 2 for 1 Bonus Offer  1987       199          0\n",
       "3  0012-1          Space Mini-Figures  1979       143         12\n",
       "4  0013-1          Space Mini-Figures  1979       143         12"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "443e967f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15705</th>\n",
       "      <td>wwgp1-1</td>\n",
       "      <td>Wild West Limited Edition Gift Pack</td>\n",
       "      <td>1996</td>\n",
       "      <td>476</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15706</th>\n",
       "      <td>XMASTREE-1</td>\n",
       "      <td>Christmas Tree</td>\n",
       "      <td>2019</td>\n",
       "      <td>410</td>\n",
       "      <td>26</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15707</th>\n",
       "      <td>XWING-1</td>\n",
       "      <td>Mini X-Wing Fighter</td>\n",
       "      <td>2019</td>\n",
       "      <td>158</td>\n",
       "      <td>60</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15708</th>\n",
       "      <td>XWING-2</td>\n",
       "      <td>X-Wing Trench Run</td>\n",
       "      <td>2019</td>\n",
       "      <td>158</td>\n",
       "      <td>52</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15709</th>\n",
       "      <td>YODACHRON-1</td>\n",
       "      <td>Yoda Chronicles Promotional Set</td>\n",
       "      <td>2013</td>\n",
       "      <td>158</td>\n",
       "      <td>413</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           set_num                                 name  year  theme_id  \\\n",
       "15705      wwgp1-1  Wild West Limited Edition Gift Pack  1996       476   \n",
       "15706   XMASTREE-1                       Christmas Tree  2019       410   \n",
       "15707      XWING-1                  Mini X-Wing Fighter  2019       158   \n",
       "15708      XWING-2                    X-Wing Trench Run  2019       158   \n",
       "15709  YODACHRON-1      Yoda Chronicles Promotional Set  2013       158   \n",
       "\n",
       "       num_parts  \n",
       "15705          0  \n",
       "15706         26  \n",
       "15707         60  \n",
       "15708         52  \n",
       "15709        413  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "9f674912",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9521</th>\n",
       "      <td>700.1-1</td>\n",
       "      <td>Extra-Large Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9534</th>\n",
       "      <td>700.2-1</td>\n",
       "      <td>Large Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9539</th>\n",
       "      <td>700.3-1</td>\n",
       "      <td>Medium Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9544</th>\n",
       "      <td>700.A-1</td>\n",
       "      <td>Small Brick Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>371</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9545</th>\n",
       "      <td>700.B-1</td>\n",
       "      <td>Small Doors and Windows Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>371</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      set_num                               name  year  theme_id  num_parts\n",
       "9521  700.1-1         Extra-Large Gift Set (ABB)  1949       365        142\n",
       "9534  700.2-1               Large Gift Set (ABB)  1949       365        178\n",
       "9539  700.3-1              Medium Gift Set (ABB)  1949       365        142\n",
       "9544  700.A-1              Small Brick Set (ABB)  1949       371         24\n",
       "9545  700.B-1  Small Doors and Windows Set (ABB)  1949       371         12"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets.sort_values('year').head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "5a8a7779",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11289</th>\n",
       "      <td>75290-1</td>\n",
       "      <td>Mos Eisley Cantina</td>\n",
       "      <td>2020</td>\n",
       "      <td>158</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5147</th>\n",
       "      <td>41430-1</td>\n",
       "      <td>Summer Fun Water Park</td>\n",
       "      <td>2020</td>\n",
       "      <td>494</td>\n",
       "      <td>1012</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11337</th>\n",
       "      <td>75550-1</td>\n",
       "      <td>Minions Kung Fu Battle</td>\n",
       "      <td>2021</td>\n",
       "      <td>689</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11335</th>\n",
       "      <td>75547-1</td>\n",
       "      <td>Minion Pilot in Training</td>\n",
       "      <td>2021</td>\n",
       "      <td>689</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11334</th>\n",
       "      <td>75546-1</td>\n",
       "      <td>Minions in Gru’s Lab</td>\n",
       "      <td>2021</td>\n",
       "      <td>689</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       set_num                      name  year  theme_id  num_parts\n",
       "11289  75290-1        Mos Eisley Cantina  2020       158          0\n",
       "5147   41430-1     Summer Fun Water Park  2020       494       1012\n",
       "11337  75550-1    Minions Kung Fu Battle  2021       689          0\n",
       "11335  75547-1  Minion Pilot in Training  2021       689          0\n",
       "11334  75546-1      Minions in Gru’s Lab  2021       689          0"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets.sort_values('year').tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "16923387",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>9521</th>\n",
       "      <td>700.1-1</td>\n",
       "      <td>Extra-Large Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9534</th>\n",
       "      <td>700.2-1</td>\n",
       "      <td>Large Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>178</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9539</th>\n",
       "      <td>700.3-1</td>\n",
       "      <td>Medium Gift Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>365</td>\n",
       "      <td>142</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9544</th>\n",
       "      <td>700.A-1</td>\n",
       "      <td>Small Brick Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>371</td>\n",
       "      <td>24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9545</th>\n",
       "      <td>700.B-1</td>\n",
       "      <td>Small Doors and Windows Set (ABB)</td>\n",
       "      <td>1949</td>\n",
       "      <td>371</td>\n",
       "      <td>12</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      set_num                               name  year  theme_id  num_parts\n",
       "9521  700.1-1         Extra-Large Gift Set (ABB)  1949       365        142\n",
       "9534  700.2-1               Large Gift Set (ABB)  1949       365        178\n",
       "9539  700.3-1              Medium Gift Set (ABB)  1949       365        142\n",
       "9544  700.A-1              Small Brick Set (ABB)  1949       371         24\n",
       "9545  700.B-1  Small Doors and Windows Set (ABB)  1949       371         12"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets[sets['year']==1949]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "9e9fc18a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>15004</th>\n",
       "      <td>BIGBOX-1</td>\n",
       "      <td>The Ultimate Battle for Chima</td>\n",
       "      <td>2015</td>\n",
       "      <td>571</td>\n",
       "      <td>9987</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11183</th>\n",
       "      <td>75192-1</td>\n",
       "      <td>UCS Millennium Falcon</td>\n",
       "      <td>2017</td>\n",
       "      <td>171</td>\n",
       "      <td>7541</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10551</th>\n",
       "      <td>71043-1</td>\n",
       "      <td>Hogwarts Castle</td>\n",
       "      <td>2018</td>\n",
       "      <td>246</td>\n",
       "      <td>6020</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>295</th>\n",
       "      <td>10256-1</td>\n",
       "      <td>Taj Mahal</td>\n",
       "      <td>2017</td>\n",
       "      <td>673</td>\n",
       "      <td>5923</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>221</th>\n",
       "      <td>10189-1</td>\n",
       "      <td>Taj Mahal</td>\n",
       "      <td>2008</td>\n",
       "      <td>673</td>\n",
       "      <td>5922</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        set_num                           name  year  theme_id  num_parts\n",
       "15004  BIGBOX-1  The Ultimate Battle for Chima  2015       571       9987\n",
       "11183   75192-1          UCS Millennium Falcon  2017       171       7541\n",
       "10551   71043-1                Hogwarts Castle  2018       246       6020\n",
       "295     10256-1                      Taj Mahal  2017       673       5923\n",
       "221     10189-1                      Taj Mahal  2008       673       5922"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets.sort_values('num_parts',ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "8e237957",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year\n",
       "1949     5\n",
       "1950     6\n",
       "1953     4\n",
       "1954    14\n",
       "1955    28\n",
       "Name: set_num, dtype: int64"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets_by_year = sets.groupby('year').count()\n",
    "sets_by_year['set_num'].head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "5242b223",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "year\n",
       "2017    786\n",
       "2018    816\n",
       "2019    840\n",
       "2020    674\n",
       "2021      3\n",
       "Name: set_num, dtype: int64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets_by_year['set_num'].tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "fc3af3b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x253285605b0>]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.plot(sets_by_year.index[:-2],sets_by_year.set_num[:-2])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "08476e40",
   "metadata": {},
   "outputs": [],
   "source": [
    "themes_by_year = sets.groupby('year').agg({'theme_id': pd.Series.nunique})"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9431698e",
   "metadata": {},
   "outputs": [],
   "source": [
    "themes_by_year.rename(columns = {'theme_id':'nr_themes'},inplace = True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "9adc52cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nr_themes</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1949</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1950</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1953</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1954</th>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1955</th>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      nr_themes\n",
       "year           \n",
       "1949          2\n",
       "1950          1\n",
       "1953          2\n",
       "1954          2\n",
       "1955          4"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "themes_by_year.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "b97f5615",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>nr_themes</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017</th>\n",
       "      <td>89</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018</th>\n",
       "      <td>93</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019</th>\n",
       "      <td>78</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020</th>\n",
       "      <td>82</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021</th>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      nr_themes\n",
       "year           \n",
       "2017         89\n",
       "2018         93\n",
       "2019         78\n",
       "2020         82\n",
       "2021          1"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "themes_by_year.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "7867d426",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Text(0, 0.5, 'number of themes')"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "ax1 = plt.gca()\n",
    "ax2 = ax1.twinx()\n",
    "plt.plot(sets_by_year.index[:-2],sets_by_year.set_num[:-2],color='g')\n",
    "plt.plot(themes_by_year.index[: -2],themes_by_year.nr_themes[:-2],'b')\n",
    "ax1.set_xlabel('year')\n",
    "ax1.set_ylabel('number of sets',color='green')\n",
    "ax2.set_ylabel('number of themes',color ='blue')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df6464f0",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "dd8216e7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1949</th>\n",
       "      <td>99.600000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1950</th>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1953</th>\n",
       "      <td>13.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1954</th>\n",
       "      <td>12.357143</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1955</th>\n",
       "      <td>36.607143</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      num_parts\n",
       "year           \n",
       "1949  99.600000\n",
       "1950   1.000000\n",
       "1953  13.500000\n",
       "1954  12.357143\n",
       "1955  36.607143"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parts_per_set = sets.groupby('year').agg({'num_parts': pd.Series.mean})\n",
    "parts_per_set.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "4ea720c1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>year</th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>2017</th>\n",
       "      <td>221.840967</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2018</th>\n",
       "      <td>213.618873</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2019</th>\n",
       "      <td>207.510714</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2020</th>\n",
       "      <td>259.732938</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2021</th>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       num_parts\n",
       "year            \n",
       "2017  221.840967\n",
       "2018  213.618873\n",
       "2019  207.510714\n",
       "2020  259.732938\n",
       "2021    0.000000"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "parts_per_set.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "c64e6f8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.collections.PathCollection at 0x253307f6f40>"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.scatter(parts_per_set.index[ :-2],parts_per_set.num_parts[: -2],color='red')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "4f67e4cd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "158    753\n",
       "501    656\n",
       "494    398\n",
       "435    356\n",
       "503    329\n",
       "Name: theme_id, dtype: int64"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "set_theme_count = sets['theme_id'].value_counts()\n",
    "set_theme_count[:5]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "28577b8c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>name</th>\n",
       "      <th>parent_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Technic</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Arctic Technic</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Competition</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Expert Builder</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Model</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   id            name  parent_id\n",
       "0   1         Technic        NaN\n",
       "1   2  Arctic Technic        1.0\n",
       "2   3     Competition        1.0\n",
       "3   4  Expert Builder        1.0\n",
       "4   5           Model        1.0"
      ]
     },
     "execution_count": 56,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "themes=pd.read_csv('themes.csv')\n",
    "themes.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "7384afe0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>id</th>\n",
       "      <th>name</th>\n",
       "      <th>parent_id</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "Empty DataFrame\n",
       "Columns: [id, name, parent_id]\n",
       "Index: []"
      ]
     },
     "execution_count": 60,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "themes[themes.name =='star Wars']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "id": "e71cb88b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>8786</th>\n",
       "      <td>65081-1</td>\n",
       "      <td>R2-D2 / C-3PO Droid Collectors Set</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12051</th>\n",
       "      <td>8000-1</td>\n",
       "      <td>Pit Droid</td>\n",
       "      <td>2000</td>\n",
       "      <td>18</td>\n",
       "      <td>223</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12058</th>\n",
       "      <td>8001-1</td>\n",
       "      <td>Battle Droid</td>\n",
       "      <td>2000</td>\n",
       "      <td>18</td>\n",
       "      <td>336</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12066</th>\n",
       "      <td>8002-1</td>\n",
       "      <td>Destroyer Droid</td>\n",
       "      <td>2000</td>\n",
       "      <td>18</td>\n",
       "      <td>567</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12071</th>\n",
       "      <td>8007-1</td>\n",
       "      <td>C-3PO</td>\n",
       "      <td>2001</td>\n",
       "      <td>18</td>\n",
       "      <td>339</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12072</th>\n",
       "      <td>8008-1</td>\n",
       "      <td>Stormtrooper</td>\n",
       "      <td>2001</td>\n",
       "      <td>18</td>\n",
       "      <td>360</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12073</th>\n",
       "      <td>8009-1</td>\n",
       "      <td>R2-D2</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>239</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12074</th>\n",
       "      <td>8010-1</td>\n",
       "      <td>Darth Vader</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>388</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12081</th>\n",
       "      <td>8011-1</td>\n",
       "      <td>Jango Fett</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>425</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12083</th>\n",
       "      <td>8012-1</td>\n",
       "      <td>Super Battle Droid</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>378</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15273</th>\n",
       "      <td>K8008-1</td>\n",
       "      <td>Darth Vader / Stormtrooper Kit</td>\n",
       "      <td>2002</td>\n",
       "      <td>18</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       set_num                                name  year  theme_id  num_parts\n",
       "8786   65081-1  R2-D2 / C-3PO Droid Collectors Set  2002        18          1\n",
       "12051   8000-1                           Pit Droid  2000        18        223\n",
       "12058   8001-1                        Battle Droid  2000        18        336\n",
       "12066   8002-1                     Destroyer Droid  2000        18        567\n",
       "12071   8007-1                               C-3PO  2001        18        339\n",
       "12072   8008-1                        Stormtrooper  2001        18        360\n",
       "12073   8009-1                               R2-D2  2002        18        239\n",
       "12074   8010-1                         Darth Vader  2002        18        388\n",
       "12081   8011-1                          Jango Fett  2002        18        425\n",
       "12083   8012-1                  Super Battle Droid  2002        18        378\n",
       "15273  K8008-1      Darth Vader / Stormtrooper Kit  2002        18          0"
      ]
     },
     "execution_count": 61,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets[sets.theme_id ==18]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 62,
   "id": "514587b1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>set_num</th>\n",
       "      <th>name</th>\n",
       "      <th>year</th>\n",
       "      <th>theme_id</th>\n",
       "      <th>num_parts</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>11013</th>\n",
       "      <td>75023-1</td>\n",
       "      <td>Star Wars Advent Calendar 2013</td>\n",
       "      <td>2013</td>\n",
       "      <td>209</td>\n",
       "      <td>254</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11046</th>\n",
       "      <td>75056-1</td>\n",
       "      <td>Star Wars Advent Calendar 2014</td>\n",
       "      <td>2014</td>\n",
       "      <td>209</td>\n",
       "      <td>273</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11080</th>\n",
       "      <td>75097-1</td>\n",
       "      <td>Star Wars Advent Calendar 2015</td>\n",
       "      <td>2015</td>\n",
       "      <td>209</td>\n",
       "      <td>291</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11131</th>\n",
       "      <td>75146-1</td>\n",
       "      <td>Star Wars Advent Calendar 2016</td>\n",
       "      <td>2016</td>\n",
       "      <td>209</td>\n",
       "      <td>282</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11173</th>\n",
       "      <td>75184-1</td>\n",
       "      <td>Star Wars Advent Calendar 2017</td>\n",
       "      <td>2017</td>\n",
       "      <td>209</td>\n",
       "      <td>309</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11206</th>\n",
       "      <td>75213-1</td>\n",
       "      <td>Star Wars Advent Calendar 2018</td>\n",
       "      <td>2018</td>\n",
       "      <td>209</td>\n",
       "      <td>307</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11245</th>\n",
       "      <td>75245-1</td>\n",
       "      <td>Star Wars Advent Calendar 2019</td>\n",
       "      <td>2019</td>\n",
       "      <td>209</td>\n",
       "      <td>280</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11281</th>\n",
       "      <td>75279-1</td>\n",
       "      <td>Star Wars Advent Calendar 2020</td>\n",
       "      <td>2020</td>\n",
       "      <td>209</td>\n",
       "      <td>312</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12019</th>\n",
       "      <td>7958-1</td>\n",
       "      <td>Star Wars Advent Calendar 2011</td>\n",
       "      <td>2011</td>\n",
       "      <td>209</td>\n",
       "      <td>267</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14352</th>\n",
       "      <td>9509-1</td>\n",
       "      <td>Star Wars Advent Calendar 2012</td>\n",
       "      <td>2012</td>\n",
       "      <td>209</td>\n",
       "      <td>235</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       set_num                            name  year  theme_id  num_parts\n",
       "11013  75023-1  Star Wars Advent Calendar 2013  2013       209        254\n",
       "11046  75056-1  Star Wars Advent Calendar 2014  2014       209        273\n",
       "11080  75097-1  Star Wars Advent Calendar 2015  2015       209        291\n",
       "11131  75146-1  Star Wars Advent Calendar 2016  2016       209        282\n",
       "11173  75184-1  Star Wars Advent Calendar 2017  2017       209        309\n",
       "11206  75213-1  Star Wars Advent Calendar 2018  2018       209        307\n",
       "11245  75245-1  Star Wars Advent Calendar 2019  2019       209        280\n",
       "11281  75279-1  Star Wars Advent Calendar 2020  2020       209        312\n",
       "12019   7958-1  Star Wars Advent Calendar 2011  2011       209        267\n",
       "14352   9509-1  Star Wars Advent Calendar 2012  2012       209        235"
      ]
     },
     "execution_count": 62,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "sets[sets.theme_id ==209]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d0130ae9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
