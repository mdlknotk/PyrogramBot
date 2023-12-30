import time
import telebot
import sqlite3
from telebot import types
from config import api_token

bot = telebot.TeleBot(api_token)

PETR1 = 'Одной из самых значимых достопримечательностей Таганрога является бронзовый памятник первому российскому императору, основателю города - Петру I. Пётр I Великий (1672–1725 гг.) – выдающийся государственный деятель, московский царь из династии Романовых, всероссийский император с 1721 года, великий реформатор. При нём Россия стала Российской империей и в государстве произошли глобальные и важные изменения. Пётр создал регулярную армию и флот, перенёс столицу в Санкт-Петербург, поделил страну на уезды и губернии. 24 года правления он провел в войнах, и отвоевал для страны выход к Балтийскому, Азовскому, Каспийскому и Чёрному морям, и сделал державу одной из величайших в свое время. Мы решили начать наш маршрут с памятника Петру, поскольку именно он положил начало городу Таганрогу. В июле 1696 года молодой царь выбрал мыс Таган - Рог на побережье Азовского моря, недалеко от устья Дона, для строительства первой военно-морской базы создававшегося российского флота. 12 сентября 1698 года Московский Пушкарский приказ, ведавший строительством крепостей, законодательно закрепил начало строительства крепости на Азовском море. Этот день считается официальной датой основания города Таганрога. Вскоре после этого была заложена одна из первых построек крепости -  церковь во имя Святой Троицы, место закладки церкви   освятили в 1699 году, в присутствии Петра I, вернувшегося из Керченского похода. Церковь дала название городу, и он в 1700 году был впервые внесён в список российских городов как Троицк на Таган - Роге. В дальнейшем за городом закрепилось географическое название - Таганрог. Таганрог как "пробный камень" петровских преобразований стал местом, где опробовались европейские методы строительства и военно-инженерного искусства, где служили первые регулярные полки русской армии и стояли первые корабли военно-морского флота. Здесь рождался новый тип российского городского населения: интернационального, многоконфессионального, поликультурного, легко принимавшего европейские новшества. Таганрожцы всегда гордились тем, что рождение их города стало одним из первых шагов царя - реформатора по пути создания Российской империи. Готовясь праздновать 200-летие Таганрога, городская общественность приняла решение об установке в городе памятника основателю и создании музея. Установленный по этой инициативе памятник, работы скульптора Марка Антокольского, стал символом Таганрога. Теперь нам бы хотелось подробнее рассказать о памятнике, возле которого мы находимся. Как мы уже сказали, установка скульптуры была приурочена к 200-летию Таганрога, случившегося в 1898 году, но процессы избрания автора для создания скульптуры и последующей её транспортировки затянулись на несколько лет. Сам же скульптор до церемонии открытия памятника не дожил. Немногие знают, но памятник Петру I много раз сменял свое место. В 1903 году на Петровской улице он был установлен, прямо перед входом в городской сад (с 1934 года и сейчас - Парк культуры и отдыха имени Горького). Памятник Петру I пережил Октябрьскую революцию и последующую волну уничтожения культурного наследия и памятников Российской империи. В январе 1924 года по указанию советских властей памятник был снят с пьедестала и перенесён в вестибюль Городской библиотеки имени А.П.Чехова. Место нового размещения было выбрано не случайно, а с целью уважить память Чехова Антона Павловича, бывшего одним из главных спонсоров установки памятника Петру I на Петровской улице.'
PETR2 = 'В 1927 году памятник Петру I был перенесён в запасники городского краеведческого музея, а пятью годами позднее, в 1932 году, зашли разговоры о том, чтобы памятник переплавить на нужды городской промышленности, однако жители Таганрога выступили против этой деструктивной затеи, а потому от неё официально отказались. А в октябре 1940 года бронзовый Пётр I работы Анткольского был даже установлен у входа в городской порт. В годы Великой Отечественной войны фашисты водрузили у входа в городской парак старый памятник Петру I. После выдворения из города оккупантов, бронзовый Пётр I был демонтирован и вновь повторил свой былой путь: недолгое время простоял в вестибюле чеховской библиотеки, затем хранился в краеведческом музее, но не в запаснике, а на виду у всех у парадного входа. Ну, а в 1948 году Пётр I был установлен на свой сохранившийся постамент у главного входа в порт Таганрога. В 1958 году его перевезли в сквер, где мы сейчас находимся. Высота бронзовой фигуры Петра I равна 3,44 метра, вес — 1232 кг. Пьедестал выполнен из гранита (одесским скульптором и владельцем художественно-бронзо-литейного завода Б. В. Эдуардсом). Высота пьедестала 5,4 метра, вес около 13 тонн. На лицевой грани пьедестала памятника выполнена надпись: «Императору Петру I-му Таганрогъ 1698 — 1898 г» Даты на пьедестале означают 200-летие Таганрога. Облик Петра I на пьедестале из гранита узнаваем: Император Пётр изображён в мундире офицера Преображенского полка. Правой рукой Пётр опирается на трость. В его левой руке зажат эфес шпаги. На груди Петра, над сердцем — орден Андрея Первозванного. От правого плеча к левому бедру грудь императора перепоясывает орденская лента. Памятник считается одним из самых запоминающихся скульптур Ростовской области. Интересный факт: Советские студенты городского радиотехнического вуза, чья военная кафедра выпускала лейтенантов Военно-Морского Флота, традиционно в ночь после защиты дипломов взбирались на скульптуру и одевали бронзовому Петру воротник матроса. Подобное изображение великого реформатора можно встретить и в других российских городах. Оригинальная гипсовая статуя Петра в натуральную величину была изготовлена Антокольским в Италии в 1872 году. Она предназначалась для Политехнической выставки в Москве, приуроченной к 200-летнему юбилею со дня рождения первого российского императора. Именно эта модель послужила образцом для изготовления ряда бронзовых отливок – как авторских, так выполненных после смерти Антокольского. Самым ранним монументом, выполненным по этой модели, стал памятник, установленный в Нижнем парке Петергофа в 1884 году (оригинал похищен фашистами в годы войны; отлитая по авторской модели копия установлена на прежнем месте в 1957 г.). Вторая скульптура была выполнена Антокольским с той же модели для Таганрога в связи с 200-летием со дня его основания.'

LENIN1 = 'Памятник В. И. Ленину – российскому революционеру, крупному теоретику марксизма, советскому политическому и государственному деятелю, создателю Российской социал-демократической рабочей партии (большевиков), главному организатору и руководителю Октябрьской революции 1917 года в России, первому Председателю Совета народных комиссаров РСФСР и Совета народных комиссаров СССР, создателю первого в мировой истории социалистического государства. Как и во многих городах бывшего СССР, в Таганроге памятник появился с целью увековечить память революционера, теоретика марксизма, основателя большевистской партии и Советского государства Владимира Ильича Ульянова (Ленина), относясь, таким образом, к скульптурной «лениниане». Бронзовая скульптура имеет высоту 4,62 метра, пьедестал — 2,74 метра. Пьедестал облицован полированными мраморными плитами. 23 января 1924г. на заседании Таганрогского окружного исполкома было принято решение о закладке в Таганроге памятника В.И. Ленину в день его похорон. После перенесения памятника Петру 1 в 1924 год, освободившийся постамент перед входом в городской сад пустовал недолго - на него в 1925 году установили памятник Ленину, созданный ленинградским скульптором Козловым Василием Васильевичем, но памятник в итоге оказался неудачным - старый постамент был слишком велик для весьма скромной по размеру скульптуры Ленина, из-за чего над памятником часто потешались мимо проходящие зеваки. Лишь в 1935 году, вскоре после преобразования городского сада в полноценный парк, был возведён новый постамент для памятника, соответствующий размерам скульптуры, и при этом расположенный ближе к входу в парк. В годы Великой Отечественной войны город Таганрог был оккупирован немцами. Фашисты уничтожили многие советские памятники в городе, не избежал этой участи и памятник Ленину у входа в городской парк - его разрушили. Кроме этого, на площади Январского восстания в 1935г. установлен памятник скульптора Д. Якерсона. Он представлял собой композицию, в которую входил броневик, на котором стоял Ленин. В годы оккупации Таганрога этот памятник был разрушен гитлеровцами. После изгнания из города оккупантов у входа в таганрогский городской парк имени Горького была установлена небольшая временная скульптура Ленина - реплика уничтоженного немцами памятника, созданная по сохранившимся фотографиям оригинала. Автором временного памятника был ростовский скульптор Гладких М.И. Временный памятник простоял до 1948 или 1949 года, пока не был заменён постоянным памятником Владимиру Ильичу Ленину, автором которого выступила советская скульптор Дрейлинг Александра Васильевна. Памятник, созданный Александрой Дрейлинг, простоял до 1970 года, пока не был демонтирован ввиду открытия нового памятника Ленину на Октябрьской площади и начавшейся реорганизации парка. Постановлением Совета Министров РСФСР № 624 от 4 декабря 1974 года памятник взят под охрану как памятник монументального искусства государственного значения, в 1992 году решение о взятии памятника на государственную охрану принял малый Совет Ростовского областного совета.'

FAINA1 = 'Памятник Фаине Раневской – российской и советской актрисе театра, кино и озвучивания, народной артистке СССР (1961), лауреату трёх Сталинских премий (1949, 1951, 1951), кавалеру ордена Ленина (1976). Фаина Раневская запомнилась многим благодаря своему неповторимому актерскому таланту. Впервые телезрители увидели Фаину Раневскую в роли колоритной госпожи Луазо в драме Михаила Ромма «Пышка». Это был 1934 год. Актрисе даже удалось побывать с этим спектаклем во Франции, куда труппу театра пригласил Ромен Роллан, чрезвычайно высоко оценивший постановку. В самом конце 30-х Раневская сыграла в трех картинах, которые сделали ее узнаваемой. Артистка воплотила в кадре образы жен. Самая популярная супруга появилась в «Подкидыше», где Раневская произнесла незабываемое и теперь уже крылатое выражение: «Муля, не нервируй меня!». В годы войны Раневская вместе с труппой театра была эвакуирована и до 1943-го работала в Ташкенте. По возвращении в Москву ей предложили сыграть Мамашу в «Свадьбе» Исидора Анненского. В этой картине Раневская снялась с известными артистами Эрастом Гариным, Зоей Федоровой, Михаилом Пуговкиным. А в 1945-м она появилась в военной музыкальной комедии «Небесный тихоход», где исполнила роль врача, профессора медицины. И вновь своим образом попала в самое яблочко. В 1947 году фильмография артистки пополнилась знаменитой комедией «Весна», в которой Раневская сыграла Маргариту Львовну. Любовь Орлова и Николай Черкасов, исполнявшие главные роли в картине, и сама Фаина Георгиевна вмиг превратили фильм в один из самых популярных и кассовых. Сценарий киноленты пролежал на полке несколько лет: авторы закончили работу над ним за 2 дня до начала войны. Впервые в «Весне» советский кинематограф опробовал спецэффекты: съемки главной героини и ее двойника в одном кадре. В том же году артистка сыграла мачеху в «Золушке». Сценарист картины Евгений Шварц обожал Раневскую. Он позволил артистке вставлять бесподобные фразы. Эта работа считается лучшей в карьере Фаины Георгиевны. В 1964-м она появилась в комедии «Легкая жизнь» вместе с Юрием Яковлевым. Сатирическую ленту снимал режиссер Вениамин Дорман. В ней Раневской удалось феноменально изобразить спекулянтку Маргариту Ивановну, которую называли Королева Марго. В итоге фильм занял 17-е место в списке самых кассовых картин того года. Последняя роль Раневской в кино — лента «Сегодня новый аттракцион». Актриса сыграла директора цирка. Любимая всеми актриса родилась в Таганроге, именно в этом городе стартовал первый международный театральный фестиваль им. Фаины Раневской «Великая провинция»., на котором 16 мая 2008 года был торжественно открыт. Памятник Фаине. На мероприятии присутствовали мэр города Таганрога, представители областной администрации, многочисленные гости, народные артисты России Евгений Стеблов и Ирина Карташева, работавшие вместе с Раневской в Театре имени Моссовета. Памятник установлен на улице Фрунзе, где мы сейчас находимся, перед памятником мы можете видеть дом, в котором прошло детство и юность актрисы (ул. Фрунзе 10 в настоящее время, в годы юности Раневской — ул. Николаевская, 12). Бронзовая скульптура изображает Раневскую в роли Ляли из фильма «Подкидыш». Высота скульптуры — 215 см. Бронзовый плинт скульптуры установлен на невысоком декоративном постаменте в виде полированной плиты из красного мрамора.'
FAINA2 = 'История вандализма:\n⚫В мае 2008 года, через несколько дней после торжественного открытия памятника, была произведена попытка «демонтажа» зонтика, который, по замыслу скульптора, мог вращаться в руке Раневской. Городские власти, оперативно отреагировав, укрепили зонтик посредством усиления конструкции и сварных соединений, исключив при этом возможность его вращения.\n⚫В начале 2009 года у зонтика Раневской была похищена ручка-набалдашник.\n⚫В июле 2009 года неизвестными вандалами была предпринята попытка вырвать из правой руки скульптурного изображения Раневской сумочку. Потерпев неудачу — сумочку удалось только искалечить — вандалы попытались отрезать или отломать саму руку. \n⚫В начале октября 2009 года вновь была предпринята попытка «демонтажа» зонтика. Зонтик «устоял», но ручка оказалась изогнутой, а сварные соединения, сделанные в 2008 году для усиления конструкции — разрушены. Восстановительные работы были проведены только в январе 2010 года, к юбилейным торжествам А.П. Чехова. \n⚫27 августа 2011 года, в день 115-летия со дня рождения Фаины Раневской, была вновь предпринята вандал-атака на зонтик: изогнута ручка, разрушено сварное соединение, вырван бант на шляпе актрисы. \n⚫Накануне 8 марта 2012 года в ходе очередной вандал-атаки на памятник зонт актрисы, так и не восстановленный с августа 2011 года, был деформирован ещё сильнее, оторвана ручка-набалдашник. \n⚫22 марта 2012 года неизвестные сорвали у памятника зонтик, пострадавший 8 марта. По мнению местной прессы, зонтик был сорван и оставлен на земле возле скульптуры после приезда одного из федеральных телеканалов. Зонтик был передан местными жителями полиции, которая намеревалась вернуть его для восстановления памятника муниципальным властям. Возвращён на место зонтик был лишь в июне 2012 года. \n⚫В начале октября 2012 года на зонтик была совершена очередная вандал-атака. Зонтик устоял, но при этом оказались разрушены отдельные сварные соединения, погнута ручка и вырвана одна спица зонта. \n⚫2 мая 2014 года в очередной раз у памятника был похищен зонтик. Восстановлен зонтик был в середине июня. \n⚫В августе 2014 года по распоряжению администрации города памятник был подвергнут варварской холодной пескоструйной обработке. В результате этой механической обработки скульптура лишилась тонкого декоративного покрытия, вскрылись все технологические швы и стала бросаться в глаза неоднородность исходного материала. Зонтик был намертво приварен к фигуре Раневской. \n'

GORDON1 = 'Водолечебница (санаторий Гордона) была основана в 1896 году доктором Николаем Герасимовичем Диварисом. Лечение ней проводилось режимом и диетой больных с заболеваниями нервной системы, болезнями обмена веществ, хронических больных, больных с застарелым сифилисом, ревматиков и др. В больнице лечили солнечными ваннами, массажем, водными процедурами и лечебной гимнастикой, позднее — электрофорезом, кумысом и кефиром. Помощником Дивариса был молодой врач Д. М. Гордон. В 1905 году семья Гордонов выкупила всю лечебницу. В 1920 году лечебница была национализирована, её бывший владелец продолжал в ней работать, занимая вплоть до самой смерти (1931 год) должность главного врача и директора. После смерти Д. М. Гордона больнице присвоили его имя.'
GORDON2 = 'Одноэтажный флигель по улице Николаевской (ныне ул. Фрунзе) был построен в конце 1880-х годах на средства купца С. К. Адабашева на участке Алферакинского квартала. Позднее Маркус Гордон, отец Д. М. Гордона, выкупил соседний участок с домом и построил на нём двухэтажное здание в стиле эклектика. Фронтон здания украшала надпись — SANATORIUM. Новое здание было соединено переходом со старым флигелем. Здание имело асимметричный трехчастный фасад со скругленными углами, украшениями в виде полуколонн и многочисленной изящной лепниной. Центральная часть здания имеет четыре колонны. В 1887 году в здании надстроили второй этаж. В здании имеются два выдвинутых вперёд боковых ризалита. На уровне второго этажа здание имеет спаренные колонны, порталы с геометрическим узором. Окна на втором этаже выполнены с циркульным завершением. В кумысолечебнице санатория Гордона в 1899 году лечился писатель А. П. Чехов. В 1918 году в доме находился штаб военного комиссара округа. С 1920 года в здании работал музей революции и археологический отдел Таганрогского краеведческого музея. В 1930-х годах в здании функционировал Горздравотдел и Санстанция. В годы Великой Отечественной войны дом занимали немцы. После войны здание опять занял Горздравотдел, потом — областная физиотерапевтическая больница.'

BANK1 = 'Здание банка было построено в 1830 году, но изначально в нем находилось здание частной аптеки, к концу 19 века семья, которой принадлежит это здание распродали имущество и новым хозяином стал Негропонте, который сдавал помещения различным компаниям и в 1895 году свои двери открыл Петербургский учетно-ссудный банк Период правления императора Александра I стал временем реформ и военных побед, именно под его правлением Россия достигла наибольшего влияния в Европе. В ходе административной реформы, создаётся Государственный Совет и министерства, происходят перемены в административно-территориальном делении империи. Особое внимание было уделено югу России. Успешной была и реформа образования, в ходе осуществления которой создавались новые университеты и гимназии. В 1806 году в Таганроге была открыта одна из старейших гимназий на юге России. Александр I подписал 31 указ, непосредственно касавшийся развития Таганрога. Все они были призваны способствовать развитию экономики, благоустройства города и края, совершенствовать систему местного управления. В мае 1818 года во время инспекционной поездки по югу России он впервые посетил Таганрог. Александр I увидел город, которому с начала царствования уделял много внимания и остался доволен увиденным. 13 сентября 1825 года Таганрог вновь встречал императора Александра I. Спустя две недели прибыла императрица Елизавета Алексеевна. Царская чета на зиму покинула Петербург, из -за болезни императрицы. Каждый день император совершал свою утреннюю прогулку, направляясь в городской сад. Он любезно раскланивался с редкими прохожими, беседовал с караульными солдатами и офицерами, дежурившими возле дворца. По свидетельству современников Александра I «в обращении был необыкновенно доступен и разговаривал на улице со многими». Жизнь в Таганроге имела особенный характер. Государь жил как частный человек, без свиты и придворного этикета, и никто из служащих без особенного приказания не мог приехать в его уединение. Заботливый муж старался исполнить любое желание Елизаветы Алексеевны. Однажды, например, императрица пожаловалась, что из городского парка плохо видно море, и Александр поручил расчистить аллею с видом на Таганрогский залив. Городской парк был создан по чертежу самого Александра и находился в собственности царской семьи. Всего в нем высадили около двух тысяч деревьев разных пород. Для содержания парка император нанял большой штат работников. 4 ноября Александр I вернулся в Таганрог тяжело больным. Как личное горе восприняли Таганрожцы болезнь императора. Каждое утро толпа горожан собиралась возле царской резиденции, чтобы узнать о состоянии его здоровья. Но усилия медиков успехом не увенчались.  19 ноября 1825 года  прервался жизненный путь российского императора Александра Благословенного. В марте 1826 года Елизавета Алексеевна, уезжая из Таганрога, подарила парк городу. По предложению градоначальника он был назван Елизаветинским.'
BANK2 = 'Увы, в 1910-х годах парк пришел в запустение, старые арендаторы отошли от дел, а в 1916-м на его территории построили аэропланный завод. Практически сразу после кончины императора, таганрогские представители донесли до Елизаветы Алексеевны желание горожан соорудить памятник Александру I. Императрица пожертвовала от себя 10 тыс. рублей. Последовали пожертвования от матери Александра Павловича - Марии Федоровны и брата - императора Николая I. Таганрожцы собрали  25 тыс. руб. Составление проекта и сооружение памятника были поручены Ивану Петровичу Мартосу, ректору Имперской Академии художеств, создателю памятника Минину и Пожарскому на Красной площади в Москве. Место установки было указано Екатериной Алексеевной – на Банковской Площади Торжественное открытие первого в России памятника Александру I состоялось 11 октября 1831 г. Когда покров был сброшен, артиллерия произвела 101 выстрел из орудий. Военные и торговые суда в гавани подняли флаги. Памятник получился красивым и торжественным. На высоком пьедестале стояла во весь рост бронзовая фигура самодержца со сводом законов в одной руке и шпагой в другой. Император попирал ногой змею, что символизировало победу над Наполеоном. Впоследствии вокруг памятника установили ограду и фонари, разбили сквер. В конце 1920-х годов памятник Александру I демонтировали и перевезли во двор дворца Александра I. В 1932 году по постановлению Таганрогского горсовета памятник отправлен в Ростов-на-Дону, где был перелит «на нужды советской промышленности». В 1998 году, к 300-летию Таганрога, памятник было решено восстановить.'

CHEKHOV1 = 'Сквер Чехова находится в Центральном районе Таганрога. Это место в старое время представляло собою часть Александровской площади, на которой, как и теперь, находился так называемый Новый базар. Помещения бывшего Гостиного двора сдавались под лавки. Одну из них снимал Павел Егорович Чехов. А. Дросси вспоминает: «Семья Чеховых проживала тогда в собственном доме на Конторской (ныне Елизаветинской) улице. Отец Антона Павловича Павел Егорович... открыл собственный магазин на Новом базаре, в котором часто можно было видеть будущего писателя, отвешивающего товары покупателям». Антон Павлович гимназистом часто бывал на Новом базаре, куда его посылала мать за провизией к обеду. На базаре он присматривался к певчим птицам и голубям, покупал их или обменивал.Эти впечатления отразились в одном из первых литературных опытов А. П. Чехова. В журнале «Досуг», издаваемом учениками гимназии, Антон Павлович поместил очерк «Сцена с натуры», действие которого происходит на Новом базаре. Многие люди знают Таганрог, именно, как родину Чехова. 17 января в семье купца на свет появляется будущий великий писатель. Антон Павлович был третьим ребенком из шести. В родительском доме всегда царили строгость и порядок, дети всегда были заняты, выполняя распределенные родителями обязанности. Каждое утро маленький Чехов с братьями и сестрами отправлялся на пение в церковном хоре. В 1868 году Антон Павлович Чехов начал учиться в гимназии, где позже он возьмет свой первый литературный псевдоним - Антоша Чехонте.  Затем Антон Павлович начал обучение в университете Москвы на медицинском факультете, который окончил в 1884 году Дебют в печати Чехова состоялся еще на первом курсе института, когда юный писатель отправил в журнал «Стрекоза» свой рассказ и юмореску. Затем в биографии Чехова было долгое путешествие на Сахалин, которое можно назвать гражданским подвигом писателя. Там он изучал жизнь ссыльных, составлял их перепись. Биография Антона Чехова содержит еще один переезд: больному туберкулезом писателю врачи рекомендовали переехать в Ялту, где климат был более подходящим для легочных больных. Здесь с ним встречаются Л. Толстой, А. Куприн, И. Бунин, И. Левитан, М. Горький. Из-за обострения болезни писатель едет в Германию для прохождения лечения, где умирает 2 июля 1904 года. В этом же году жители Таганрога обратились в городскую управу с прошением об установке памятника их великому земляку. Решение о создании памятника было принято в 1910 году и начался сбор средств. Решение о сооружении памятника было принято 18 июня 1910 года. В этом же году было получено Высочайшее соизволение на всероссийскую подписку на сбор средств для создания памятника, образован комитет по сбору пожертвований и проектированию памятника. Подписные листы были напечатаны в таганрогской типографии А. Б. Тараховского, там были указаны фамилии жертвователей и сумма средств, внесённая каждым из них. Имена пожертвовавших средства планировалось публиковать в местных газетах. На просьбу таганрогжцев откликнулись во многих городах России. Так, например, на создание памятника был перечислен весь сбор с лекции «Поэзия как волшебство», которую прочитал в зале Общественного собрания Таганрога поэт Константин Бальмонт. Однако в царской России памятник Чехову так и не был установлен, реализовать эту идею помешала сначала Первая мировая, а затем Гражданская война.'
CHEKHOV2 = 'К 1 января 1920 года для этой цели было собрано 8822 рубля 60 копеек. Однако до середины 30-х годов о памятнике не вспоминали. Лишь в июле 1934, на городском литературном вечере, посвящённом 30-летию со дня смерти писателя, вновь объявили о сооружении в Таганроге памятника Чехову к его 75-летнему юбилею.В январе 1935 года «решением центральных организаций ознаменование чеховской годовщины общественно-культурными мероприятиями» было перенесено на май и «сосредоточено в Таганроге». Во время праздничных мероприятий планировалось осуществить закладку памятника Чехову. В годы Великой Отечественной войны, в связи с 40-летием со дня смерти писателя, Совет народных комиссаров СССР принял новое постановление о сооружении памятников Чехову в Москве и Таганроге. В итоге, к идее установки памятника вернулись только в 1960 году. Автором проекта стал скульптор Иулиан Рукавишников. Высота скульптуры Антона Чехова в сквере Чехова составляет 3 метра. Пьедестал памятника покрыт мраморными плитами. Всего в России насчитывается более 30 памятников Чехова и героям его рассказов. «Таганрогский театр имени А.П. Чехова» - один из старейших на юге России. Здание таганрогского театра было построено на главной улице города в 1866 году, однако его история восходит к гораздо более раннему времени – к самому началу XIX столетия. Первый камень в основание нового здания заложили 2 апреля 1866 года. А строительство здания городского оперного театра с великолепной акустикой было завершено в головокружительно короткие сроки: спустя 8 месяцев, 25 ноября 1866 года состоялось его торжественное открытие. Театр родного города оказал колоссальное влияние на будущего писателя, вызвал у него интерес к драматургии: многие рассказы, фельетоны, рецензии, статьи и письма Чехова 1880-х годов посвящены театру и актерам. Еще при жизни Чехова на таганрогской сцене были поставлены все его произведения, начиная с водевиля "Медведь", показанного на благотворительном вечере 17 января 1890 года, и заканчивая пьесой "Вишневый сад", привезенной в Таганрог ростовской труппой в марте 1904 года - в год смерти писателя.'
CHEKHOV3 ='Истории вандализма:\n⚫В мае 2023 года Неизвестный водитель по какой-то причине наехал на постамент памятника Антону Павловичу Чехову и повредил газон вокруг изваяния. По неустановленной причине автомобилист на скорости заехал на территорию сквера в центре города, которую организовали в честь русского писателя. Водитель немного сдвинул с места гранитные плиты и повредил газон.'

LOCSTR = 'Нажмите на виджет ниже, чтобы построить маршрут⬇️'

conn = sqlite3.connect('db/userlist.db', check_same_thread=False)
cursor = conn.cursor()

def db_table_val(user_id: int, user_name: str, user_surname: str, username: str, language: SyntaxError):
	cursor.execute('INSERT OR REPLACE INTO test (user_id, user_name, user_surname, username, language) VALUES (?, ?, ?, ?, ?)', (user_id, user_name, user_surname, username, language))
	conn.commit()

@bot.message_handler(commands = ['start'])
def url(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Начать🏟️')
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Нажмите кнопку, чтобы начать⬇️", reply_markup = markup)

cNO = 0

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global cNO
    match message.text:
        case 'Начать🏟️': 
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton(text='Да✅')
            btn2 = types.KeyboardButton(text='Нет❌')
            markup.add(btn1,btn2)
            bot.send_message(message.from_user.id,"Приветсвуем в чат-боте TagEx")
            time.sleep(0.5)
            bot.send_message(message.from_user.id,"Вы согласны на сбор необязательной информации?",reply_markup=markup)
            us_id = message.from_user.id
            us_name = message.from_user.first_name
            us_sname = message.from_user.last_name
            username = message.from_user.username
            lang = message.from_user.language_code
            db_table_val(user_id=us_id, user_name=us_name, user_surname=us_sname, username=username,language = lang)
            print('User ' +  str(message.from_user.id) + ' checked in')


        case 'Да✅' | 'Нет❌'|'Выбрать другой город🏙️(В разработке)':
               time.sleep(0.5)
               markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
               btn1 = types.KeyboardButton(text='Таганрог')
               markup.add(btn1)
               bot.send_message(message.from_user.id,"Выберите город для проведения экскурсии",reply_markup=markup)
        case 'Таганрог'| 'Вернуться назад↩️': 
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Памятник Петру I')
                btn2 = types.KeyboardButton(text='Памятник Ленину')
                btn3 = types.KeyboardButton(text='Памятник Фаине Раневской')
                btn5 = types.KeyboardButton(text='Банковская площадь и памятник Александру I')
                btn6 = types.KeyboardButton(text='Памятник Антону Чехову')
                btn7 = types.KeyboardButton(text='Выбрать другой город🏙️(В разработке)')
                
                markup.add(btn1,btn2,btn3,btn5,btn6,btn7)
                bot.send_message(message.from_user.id,"Выберите желаемую достопримечательность:",reply_markup=markup)
                print('User ' +  str(message.from_user.id) + ' Is currently on Таганрог')


        case 'Памятник Петру I':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Вернуться назад↩️')
                markup.add(btn1)
                bot.send_photo(message.from_user.id,'https://upload.wikimedia.org/wikipedia/commons/0/07/2008_Peter_the_Great_Monument.jpg')
                bot.send_message(message.from_user.id,PETR1)
                bot.send_message(message.from_user.id,PETR2)
                bot.send_message(message.from_user.id,LOCSTR,reply_markup=markup)
                bot.send_location(message.from_user.id,latitude=47.205009,longitude=38.946356)
                print('User ' +  str(message.from_user.id) + ' Is currently on '+ message.text)
        case 'Памятник Ленину':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Вернуться назад↩️')
                markup.add(btn1)
                bot.send_photo(message.from_user.id,'https://upload.wikimedia.org/wikipedia/commons/4/41/Taganrog_Pamyatn_Lenin_2012_01.jpg')
                bot.send_message(message.from_user.id,LENIN1)
                bot.send_message(message.from_user.id,LOCSTR,reply_markup=markup)
                bot.send_location(message.from_user.id,latitude=47.208888,longitude=38.936349)
                print('User ' +  str(message.from_user.id) + ' Is currently on '+ message.text)
        case 'Памятник Фаине Раневской':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Вернуться назад↩️')
                markup.add(btn1)
                bot.send_photo(message.from_user.id,'https://sudakov.travel/images/editor/points-of-interest/Pamyatnik-Faine-Ranevskoj-v-Taganroge-min.jpg')
                bot.send_message(message.from_user.id,FAINA1)
                bot.send_message(message.from_user.id,FAINA2)
                bot.send_message(message.from_user.id,LOCSTR,reply_markup=markup)
                bot.send_location(message.from_user.id,latitude=47.210650,longitude=38.933651)
                print('User ' +  str(message.from_user.id) + ' Is currently on '+ message.text)
        case 'Банковская площадь и памятник Александру I':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Вернуться назад↩️')
                markup.add(btn1)
                bot.send_photo(message.from_user.id,'https://media-cdn.tripadvisor.com/media/photo-s/1a/fd/5b/12/i.jpg')
                bot.send_message(message.from_user.id,BANK1)
                bot.send_message(message.from_user.id,BANK2)
                bot.send_message(message.from_user.id,LOCSTR,reply_markup=markup)
                bot.send_location(message.from_user.id,latitude=47.211880,longitude=38.926988)
                print('User ' +  str(message.from_user.id) + ' Is currently on '+ message.text)
        case 'Памятник Антону Чехову':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton(text='Вернуться назад↩️')
                markup.add(btn1)
                bot.send_photo(message.from_user.id,'https://yugarf.ru/wp-content/uploads/2018/11/pamyatnik-chehovu-v-taganroge.jpg')
                bot.send_message(message.from_user.id,CHEKHOV1)
                bot.send_message(message.from_user.id,CHEKHOV2)
                bot.send_message(message.from_user.id,CHEKHOV3)
                bot.send_message(message.from_user.id,LOCSTR,reply_markup=markup)
                bot.send_location(message.from_user.id,latitude=47.210497,longitude=38.922348)
                print('User ' +  str(message.from_user.id) + ' Is currently on '+ message.text)
                  
                
                



bot.polling(none_stop=True, interval=0)