
Marriage Equality in the US
===========================

National Opinion Research Center Data from NORC General Social Survey
http://www3.norc.org/GSS+Website/Download/

The data fields are described here:
http://publicdata.norc.org:41000/gss/documents//BOOK/GSS\_Codebook\_index.pdf

Relevant columns:

-  **MARHOMO** HOMOSEXUALS SHOULD HAVE RIGHT TO MARRY
-  **HOMOSEX1** IS HOMOSEXUAL SEX WRONG?
-  **HOMOCHNG**
-  **SEXORNT**
-  **MARUNION**

   GAYS AND LESBIANS Age first attracted to same sex ATTRACTD Age R
   first told another that R was gay/les/bi TOLDSXOR Age R first told
   another R had sex with same sex TOLDSMSX Attitudes toward HOMOSEX,
   HOMOSEX1 Cause of homosexuality HOMOCHNG Civil liberties of SPKHOMO,
   COLHOMO, LIBHOMO Gender of R's sex partners since age 18 SEXSEX18
   Government inquiries into ASKSEXOR Housing problems due to
   discrimination EVDWELL, DWELL5 In military DRAFTGAY Job Harassment
   EVHARJB, HARJOB5 How many co-workers know R is gay TOLDWORK Job
   loss/problems due to discrimination EVLOSEJB, LOSEJOB5, EVNEGJOB,
   NEGJOB5 Marriage MARHOMO Marital status of R MARUNION Number of Gays
   R knows… at work ACQWKGAY, TOLDWORK in family ACQFMGAY in general
   ACQGAY in neighborhood ACQNHGAY through voluntary organizations
   ACQVAGAY Number if Gays R trusts TRTGAY Sexual orientation of R
   SEXORNT Spouse/partner, sex of SEXUNION

This is hard to geographically disambiguate, as the geo information is
withheld. To get it, need to fill out some forms, send in money, etc.
http://publicdata.norc.org:41000/gss/documents//OTHR/ObtainingGSSSensitiveDataFiles.pdf

.. code:: python

    import pandas as pd

.. code:: python

    gss = pd.read_stata('/Users/houghtons/Desktop/Data/GSS/GSS2012.DTA')
    gss.head()




.. raw:: html

    <div style="max-height:1000px;max-width:1500px;overflow:auto;">
    <table border="1" class="dataframe">
      <thead>
        <tr style="text-align: right;">
          <th></th>
          <th>year</th>
          <th>id</th>
          <th>wtss</th>
          <th>vpsu</th>
          <th>vstrat</th>
          <th>res2008</th>
          <th>res2010</th>
          <th>isco88</th>
          <th>spisco88</th>
          <th>paisco88</th>
          <th>...</th>
          <th>wrksch</th>
          <th>wrkslf</th>
          <th>wrkstat</th>
          <th>wrkwayup</th>
          <th>wwwhr</th>
          <th>wwwmin</th>
          <th>xmarsex</th>
          <th>xmovie</th>
          <th>xnorcsiz</th>
          <th>zodiac</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <th>0</th>
          <td> 2012</td>
          <td> 1</td>
          <td> 2.621963</td>
          <td> 1</td>
          <td> 3001</td>
          <td> living in the u.s.</td>
          <td> living in the u.s.</td>
          <td> 3429</td>
          <td>  NaN</td>
          <td> 1233</td>
          <td>...</td>
          <td> work part-time</td>
          <td> someone else</td>
          <td> working parttime</td>
          <td> agree somewhat</td>
          <td>  5</td>
          <td>NaN</td>
          <td>     always wrong</td>
          <td> NaN</td>
          <td> uninc,med city</td>
          <td>     libra</td>
        </tr>
        <tr>
          <th>1</th>
          <td> 2012</td>
          <td> 2</td>
          <td> 3.495950</td>
          <td> 1</td>
          <td> 3001</td>
          <td> living in the u.s.</td>
          <td> living in the u.s.</td>
          <td> 3132</td>
          <td>  NaN</td>
          <td>  NaN</td>
          <td>...</td>
          <td>            NaN</td>
          <td> someone else</td>
          <td> working parttime</td>
          <td>            NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td>     always wrong</td>
          <td> yes</td>
          <td> uninc,med city</td>
          <td>     aries</td>
        </tr>
        <tr>
          <th>2</th>
          <td> 2012</td>
          <td> 3</td>
          <td> 1.747975</td>
          <td> 1</td>
          <td> 3001</td>
          <td> living in the u.s.</td>
          <td> living in the u.s.</td>
          <td> 2144</td>
          <td> 2331</td>
          <td>  NaN</td>
          <td>...</td>
          <td>            NaN</td>
          <td> someone else</td>
          <td> working fulltime</td>
          <td>            NaN</td>
          <td>NaN</td>
          <td>NaN</td>
          <td> almst always wrg</td>
          <td> yes</td>
          <td> uninc,med city</td>
          <td>     aries</td>
        </tr>
        <tr>
          <th>3</th>
          <td> 2012</td>
          <td> 4</td>
          <td> 1.235694</td>
          <td> 1</td>
          <td> 3001</td>
          <td> living in the u.s.</td>
          <td> living in the u.s.</td>
          <td> 2411</td>
          <td> 1233</td>
          <td> 1210</td>
          <td>...</td>
          <td>            NaN</td>
          <td> someone else</td>
          <td>            other</td>
          <td> agree strongly</td>
          <td> 15</td>
          <td>NaN</td>
          <td>              NaN</td>
          <td>  no</td>
          <td> uninc,med city</td>
          <td> capricorn</td>
        </tr>
        <tr>
          <th>4</th>
          <td> 2012</td>
          <td> 5</td>
          <td> 0.873988</td>
          <td> 1</td>
          <td> 3001</td>
          <td> living in the u.s.</td>
          <td> living in the u.s.</td>
          <td> 5163</td>
          <td>  NaN</td>
          <td> 1319</td>
          <td>...</td>
          <td> work full-time</td>
          <td> someone else</td>
          <td>          retired</td>
          <td> agree strongly</td>
          <td>  4</td>
          <td>  0</td>
          <td>              NaN</td>
          <td>  no</td>
          <td> city,50-250000</td>
          <td>    taurus</td>
        </tr>
      </tbody>
    </table>
    <p>5 rows × 818 columns</p>
    </div>



.. code:: python

    gss.columns.values




.. parsed-literal::

    array(['year', 'id', 'wtss', 'vpsu', 'vstrat', 'res2008', 'res2010',
           'isco88', 'spisco88', 'paisco88', 'maisco88', 'mar1', 'mar2',
           'mar3', 'mar4', 'mar5', 'mar6', 'mar7', 'mar8', 'mar11', 'mar12',
           'mar13', 'mar14', 'abany', 'abdefect', 'abhlth', 'abnomore',
           'abpoor', 'abrape', 'absingle', 'accntsci', 'accptoth', 'acqntsex',
           'actupset', 'adults', 'advfront', 'affrmact', 'age', 'aged',
           'agekdbrn', 'architct', 'arrest', 'astrolgy', 'astrosci', 'attend',
           'away1', 'away11', 'away12', 'away2', 'away3', 'away4', 'away5',
           'away6', 'away7', 'away8', 'babies', 'ballot', 'balneg', 'balpos',
           'barate', 'betrlang', 'bible', 'bigbang', 'bigbang1', 'biosci',
           'bmitzvah', 'born', 'bossemps', 'boyorgrl', 'cappun', 'carecost',
           'careprov', 'careself', 'caresik1', 'carried', 'childs', 'chldidel',
           'class', 'closeblk', 'closewht', 'cmprgmng', 'cohabok', 'cohort',
           'colath', 'colcom', 'coldeg1', 'colhomo', 'colmil', 'colmslm',
           'colrac', 'colsci', 'colscinm', 'comprend', 'compuse', 'conarmy',
           'conbus', 'conclerg', 'condom', 'condrift', 'coneduc', 'confed',
           'confinan', 'coninc', 'conjudge', 'conlabor', 'conlegis',
           'conmedic', 'conpress', 'conrinc', 'consci', 'consent', 'contv',
           'convictd', 'cooking1', 'coop', 'courts', 'crack30', 'cshutyp08',
           'cshutyp10', 'cutahead', 'dateintv', 'deckids', 'degree', 'denom',
           'denom16', 'denyrais', 'difstand', 'dipged', 'directns', 'discaff',
           'discaffm', 'discaffw', 'divbest', 'divlaw', 'divorce', 'dwell5',
           'dwelling', 'dwelown', 'earnrs', 'earnshh', 'earthsun', 'econsci',
           'educ', 'eftotlt', 'eharaswk', 'eldcost', 'eldersup', 'eldhelp',
           'electron', 'emailhr', 'emailmin', 'engbrng', 'engbtr', 'engda',
           'engdgr', 'engdo', 'engearn', 'engfun', 'enggood', 'engint',
           'englone', 'engnring', 'engnrsci', 'engodd', 'engprob', 'engrel',
           'engresp', 'engson', 'eqwlth', 'eth1', 'eth2', 'eth3', 'ethnic',
           'ethnum', 'evcrack', 'evdwell', 'evharjb', 'evidu', 'evlosejb',
           'evnegjob', 'evolved', 'evolved1', 'evpaidsx', 'evstray', 'evwork',
           'expdesgn', 'exptext', 'fair', 'fambudgt', 'famdif16', 'famgen',
           'family16', 'famsuffr', 'famvswk1', 'famwkbst', 'famwklst',
           'farming', 'fear', 'fechld', 'feelevel', 'feeused', 'fefam',
           'fehire', 'fejobaff', 'fepol', 'fepresch', 'finalter', 'finlcoun',
           'finrela', 'fireftng', 'form', 'formwt', 'frndsex', 'fucitzn',
           'fund', 'fund16', 'gender1', 'gender10', 'gender11', 'gender12',
           'gender13', 'gender14', 'gender2', 'gender3', 'gender4', 'gender5',
           'gender6', 'gender7', 'gender8', 'gender9', 'getahead', 'givblood',
           'givchrty', 'givhmlss', 'givseat', 'god', 'goodlife', 'gradtounder',
           'granborn', 'grass', 'gunlaw', 'hapcohab', 'hapmar', 'happy',
           'happy7', 'harjob5', 'health', 'health1', 'hefinfo', 'helpaway',
           'helpblk', 'helpful', 'helphwrk', 'helpjob', 'helpnot', 'helpoth',
           'helppoor', 'helpsick', 'hhclean1', 'hhrace', 'hhtype', 'hhtype1',
           'hhwkfair', 'hispanic', 'histsci', 'hivtest', 'hivtest1',
           'hivtest2', 'homekid', 'homosex', 'hompop', 'hotcore', 'housewrk',
           'hrs1', 'hrs2', 'hsbio', 'hschem', 'hsmath', 'hsphys', 'hubbywk1',
           'hunt', 'idu30', 'if08who', 'ignorwk', 'incom16', 'income',
           'income06', 'indus10', 'intage', 'intecon', 'inteduc', 'intenvir',
           'intethn', 'intfarm', 'inthisp', 'intid', 'intintl', 'intlblks',
           'intlwhts', 'intmed', 'intmil', 'intrace1', 'intrace2', 'intrace3',
           'intrhome', 'intsci', 'intsex', 'intspace', 'inttech', 'intyrs',
           'issp', 'jew', 'jew16', 'jew16aj', 'jewaj', 'jobfind', 'jobhour',
           'jobinc', 'joblose', 'jobmeans', 'jobpromo', 'jobsec', 'jobsecok',
           'jobvsfa1', 'jokeswk', 'journlsm', 'kd1jwoth', 'kd1relig',
           'kd2jwoth', 'kd2relig', 'kd3relig', 'kidfinbu', 'kidjob', 'kidjoy',
           'kidnofre', 'kidnum', 'kidsocst', 'kidssol', 'kidsuffr', 'lackinfo',
           'lasers', 'laundry1', 'lawenfrc', 'lentto', 'letdie1', 'letin1',
           'libath', 'libcom', 'libhomo', 'libmil', 'libmslm', 'librac',
           'liedcwkr', 'life', 'liveblks', 'livewhts', 'lngthinv', 'loanitem',
           'localnum', 'lockedup', 'lookaway', 'losejob5', 'madeg', 'maeduc',
           'maind10', 'majew', 'major1', 'major2', 'majorcol', 'majwoth',
           'maocc10', 'marasian', 'marblk', 'marelig', 'marhappy', 'marhisp',
           'marhomo', 'marital', 'marlegit', 'marrcoun', 'marwht', 'matesex',
           'mawork14', 'mawrkgrw', 'mawrkslf', 'mawrkwrm', 'medsci',
           'medtreat', 'meovrwrk', 'mntlhlth', 'mobile16', 'mode', 'nataid',
           'nataidy', 'natarms', 'natarmsy', 'natchld', 'natcity', 'natcityy',
           'natcrime', 'natcrimy', 'natdrug', 'natdrugy', 'nateduc',
           'nateducy', 'natenrgy', 'natenvir', 'natenviy', 'natfare',
           'natfarey', 'natheal', 'nathealy', 'natmass', 'natpark', 'natrace',
           'natracey', 'natroad', 'natsci', 'natsoc', 'natspac', 'natspacy',
           'negjob5', 'news', 'newsfrom', 'nextgen', 'numcong', 'numemps',
           'numkids', 'nummen', 'numwomen', 'obey', 'occ10', 'odds1', 'odds2',
           'old1', 'old10', 'old11', 'old12', 'old13', 'old14', 'old2', 'old3',
           'old4', 'old5', 'old6', 'old7', 'old8', 'old9', 'oth16', 'othcredt',
           'other', 'othersex', 'othjew', 'othjew16', 'othlang', 'othlang1',
           'othlang2', 'othshelp', 'oversamp', 'owngun', 'padeg', 'paeduc',
           'paidlv', 'paidlv1', 'paidlvdv', 'paidlvpy', 'paidsex', 'paind10',
           'pajew', 'pajwoth', 'paocc10', 'parborn', 'parelig', 'parsol',
           'partfull', 'partners', 'partnrs5', 'partyid', 'pawrkslf',
           'peoptrbl', 'phase', 'phone', 'physcsci', 'pikupsex', 'pillok',
           'pistol', 'polabuse', 'polattak', 'poleff11', 'poleff13',
           'poleff15', 'poleff16', 'poleff17', 'poleff3', 'polefy11',
           'polefy13', 'polefy15', 'polefy16', 'polefy17', 'polefy3',
           'polescap', 'polhitok', 'polmurdr', 'polviews', 'popespks',
           'popular', 'pornlaw', 'posslq', 'posslqy', 'postlife', 'pray',
           'prayer', 'premarsx', 'pres08', 'prespop', 'preteen', 'putdown',
           'racdif1', 'racdif2', 'racdif3', 'racdif4', 'race', 'racecen1',
           'racecen2', 'racecen3', 'raclive', 'racopen', 'racwork', 'radioact',
           'rank', 'ratetone', 'realinc', 'realrinc', 'reborn', 'reg16',
           'region', 'relactiv', 'relate1', 'relate10', 'relate11', 'relate12',
           'relate13', 'relate14', 'relate2', 'relate3', 'relate4', 'relate5',
           'relate6', 'relate7', 'relate8', 'relate9', 'relatsex', 'relhh1',
           'relhh10', 'relhh11', 'relhh12', 'relhh13', 'relhh14', 'relhh2',
           'relhh3', 'relhh4', 'relhh5', 'relhh6', 'relhh7', 'relhh8',
           'relhh9', 'relhhd1', 'relhhd10', 'relhhd11', 'relhhd12', 'relhhd13',
           'relhhd14', 'relhhd2', 'relhhd3', 'relhhd4', 'relhhd5', 'relhhd6',
           'relhhd7', 'relhhd8', 'relhhd9', 'relig', 'relig16', 'reliten',
           'relpersn', 'relsp1', 'relsp10', 'relsp11', 'relsp12', 'relsp13',
           'relsp14', 'relsp2', 'relsp3', 'relsp4', 'relsp5', 'relsp6',
           'relsp7', 'relsp8', 'relsp9', 'repairs1', 'res16', 'respnum',
           'retchnge', 'rfamlook', 'rhhwork', 'richwork', 'rifle', 'rincom06',
           'rincome', 'rowngun', 'rplace', 'rudewk', 'rumorwk', 'rvisitor',
           'sampcode', 'sample', 'satfam7', 'satfin', 'satjob', 'satjob7',
           'savesoul', 'scibnfts', 'sciental', 'scientbe', 'scientbr',
           'scientda', 'scientdn', 'scientdo', 'scientfu', 'scientgo',
           'scienthe', 'scientmo', 'scientod', 'scientr', 'scientre',
           'scientsn', 'scientwk', 'scifrom', 'scinews1', 'scinews2',
           'scinews3', 'scistudy', 'scitext', 'sector', 'seeksci', 'selffrst',
           'selfless', 'sex', 'sexeduc', 'sexfreq', 'sexornt', 'sexsex',
           'sexsex18', 'sexsex5', 'shop1', 'shotgun', 'shout', 'sibs',
           'singlpar', 'size', 'slsmnshp', 'socbar', 'socfrend', 'socommun',
           'socrel', 'socsci', 'solarrev', 'spaneng', 'spanint', 'spanking',
           'spanself', 'spbarate', 'spdeg', 'spden', 'spdipged', 'speduc',
           'speftotlt', 'spevwork', 'spfalook', 'spfund', 'spgradtounder',
           'sphhwork', 'sphrs1', 'sphrs2', 'spind10', 'spjew', 'spjew16',
           'spjewaj', 'spjoth16', 'spkath', 'spkcom', 'spkhomo', 'spklang',
           'spkmil', 'spkmslm', 'spkrac', 'splive', 'spocc10', 'spother',
           'spothjew', 'sprel', 'sprel16', 'sprtprsn', 'spsector', 'spwrkslf',
           'spwrksta', 'srcbelt', 'ssfchild', 'ssmchild', 'suicide1',
           'suicide2', 'suicide3', 'suicide4', 'supcares', 'synmem',
           'talkedto', 'tax', 'teens', 'teensex', 'thnkself', 'ticket',
           'tiredhm1', 'tiredwk1', 'toldwork', 'toofast', 'treatres', 'trust',
           'trynewjb', 'tvhours', 'twoincs1', 'unemp', 'union', 'unrelat',
           'uscitzn', 'usewww', 'uswar', 'uswary', 'version', 'vetyears',
           'viruses', 'visart', 'visitors', 'vislib', 'visnhist', 'vissci',
           'viszoo', 'voedcol', 'voedncol', 'voednme1', 'voednme2', 'volacty2',
           'volactyr', 'volchrty', 'volmonth', 'vote08', 'webmob', 'weekswrk',
           'whencol', 'whenhs', 'where1', 'where11', 'where12', 'where2',
           'where3', 'where4', 'where5', 'where6', 'where7', 'where8',
           'whoelse1', 'whoelse2', 'whoelse3', 'whoelse4', 'whoelse5',
           'whoelse6', 'widowed', 'wkageism', 'wkbhvrs', 'wkkidscl',
           'wkkidscs', 'wkndact', 'wkracism', 'wkrspns', 'wkstress', 'wksub',
           'wksubs', 'wksup', 'wksups', 'wkvsfam', 'wkyngscl', 'wkyngscs',
           'wlthblks', 'wlthwhts', 'worda', 'wordb', 'wordc', 'wordd', 'worde',
           'wordf', 'wordg', 'wordh', 'wordi', 'wordj', 'wordsum', 'workblks',
           'workhard', 'workwhts', 'wrkbaby', 'wrkgovt', 'wrksch', 'wrkslf',
           'wrkstat', 'wrkwayup', 'wwwhr', 'wwwmin', 'xmarsex', 'xmovie',
           'xnorcsiz', 'zodiac'], dtype=object)



.. code:: python

    gss['age']




.. parsed-literal::

    0     22
    1     21
    2     42
    3     49
    4     70
    5     50
    6     35
    7     24
    8     28
    9     28
    10    55
    11    36
    12    28
    13    59
    14    52
    ...
    1959    63
    1960    20
    1961    71
    1962    50
    1963    23
    1964    65
    1965    60
    1966    69
    1967    78
    1968    25
    1969    61
    1970    53
    1971    48
    1972    37
    1973    22
    Name: age, Length: 1974, dtype: object



.. code:: python

    gss['marhomo']





.. parsed-literal::

    0                 strongly agree
    1              strongly disagree
    2                 strongly agree
    3                            NaN
    4                            NaN
    5                 strongly agree
    6                            NaN
    7                 strongly agree
    8     neither agree nor disagree
    9                 strongly agree
    10                           NaN
    11                           NaN
    12                strongly agree
    13             strongly disagree
    14                           NaN
    ...
    1959                strongly agree
    1960                strongly agree
    1961                           NaN
    1962                         agree
    1963                strongly agree
    1964                           NaN
    1965                         agree
    1966                           NaN
    1967                      disagree
    1968                strongly agree
    1969                           NaN
    1970             strongly disagree
    1971    neither agree nor disagree
    1972                           NaN
    1973    neither agree nor disagree
    Name: marhomo, Length: 1974, dtype: object



