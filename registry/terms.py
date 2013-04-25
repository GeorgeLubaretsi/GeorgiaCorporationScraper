# -*- coding: utf-8 -*-
positions = set([u"პარტნიორი",
             u"შეზღუდული პარტნიორები",
             u"სრული პარტნიორები",
             u"ხელმძღვანელი",
             u"კომანდიტი",
             u"კომპლემენტარი",
             u"დამფუძნებელი/დამფუძნებლები",
             u"დირექტორი",
             u"წარმომადგენელი",
             u"პარტნიორთა კრება",
             u"დირექტორი",
             u"დამფუძნებელი",
             u"პარტნიორები",
             u"ინდივიდუალური მეწარმე",
             u"დამფუძნებელი",
             u"გამგეობის წევრი",
             u"ხელმძღვანელობაზე/წარმომადგენლობაზე უფლებამოსილი პირები",
             u"თავმჯდომარე",
             u"პრეზიდენტი",
             u"გამგეობის წევრი",
             u"მოადგილე",
             u"გამგეობის წევრი",
             u"მენეჯერი",
             u"ხელმძღვანელი",
             u"დირექტორი",
             u"გენერალური დირექტორი",
             u"საოპერაციო დირექტორი",
             u"დირექტორი",
             u"წარმომადგენელი",
             u"ხელმძღვანელი",
             u"თავმჯდომარე",
             u"დამფუძნებელი",
             u"დამფუძნებელი",
             u"აქციონერი/აქციონერები",
             u"აღმასრულებელი დირექტორი",
             u"განმცხადებელი",
             u"სამეთვალყურეო საბჭოს წევრი",
             u"სავაჭრო წარმომადგენელი",
             u"წარმომადგენელთა კრების წევრი",])

nationalities = set([
u"ავსტრალია",
u"ავსტრია",
u"ავღანეთი",
u"აზერბაიჯანი",
u"ალბანეთი",
u"ალჟირი",
u"ამერიკის სამოა",
u"ამერიკის ვირჯინიის კუნძულები",
u"ამერიკის შეერთებული შტატები",
u"ანგილია",
u"ანგოლა",
u"ანდორა",
u"ანტიგუა და ბარბუდა",
u"არაბთა გაერთიანებული საამიროები",
u"არგენტინა",
u"არუბა",
u"აღმოსავლეთი ტიმორი",
u"ახალი ზელანდია",
u"ახალი კალედონია",
u"ბანგლადეში",
u"ბარბადოსი",
u"ბასას-და-ინდია",
u"ბაჰამის კუნძულები",
u"ბაჰრეინი",
u"ბელარუსი",
u"ბელგია",
u"ბელიზი",
u"ბენინი",
u"ბერმუდა",
u"ბოლივია",
u"ბოსნია და ჰერცეგოვინა",
u"ბოტსვანა",
u"ბრაზილია",
u"ბრიტანეთის ვირჯინიის კუნძულები",
u"ბრიტანეთის ინდოეთის ოკეანის ტერიტორია",
u"ბრუნეი",
u"ბულგარეთი",
u"ბურკინა ფასო",
u"ბურუნდი",
u"ბუვე",
u"ბჰუტანი",
u"გაბონი",
u"გაიანა",
u"გამბია",
u"განა",
u"გერმანია",
u"გვადელუპა",
u"გვატემალა",
u"გვინეა",
u"გვინეა-ბისაუ",
u"გიბრალტარი",
u"გლორიოზოს კუნძულები",
u"გრენადა",
u"გრენლანდია",
u"გუამი",
u"დანია",
u"დიდი ბრიტანეთი",
u"დომინიკელთა რესპუბლიკა",
u"დომინიკა",
u"ეგვიპტე",
u"ევროპა (კუნძული)",
u"ეთიოპია",
u"ეკვადორი",
u"ეკვატორული გვინეა",
u"ერაყი",
u"ერიტრეა",
u"ესპანეთი",
u"ესტონეთი",
u"ეშმორის და კარტიეს კუნძულები",
u"ვალისი და ფუტუნა",
u"ვანუატუ",
u"ვატიკანი",
u"ვენესუელა",
u"ვიეტნამი",
u"ზამბია",
u"ზიმბაბვე",
u"თურქეთი",
u"თურქმენეთი",
u"იამაიკა",
u"იან მაიენი",
u"იაპონია",
u"იემენი",
u"ინდოეთი",
u"ინდონეზია",
u"იორდანია",
u"ირანი",
u"ირლანდია",
u"ისლანდია",
u"ისრაელი",
u"იტალია",
u"კაბო-ვერდე",
u"კაიმანის კუნძულები",
u"კამბოჯა",
u"კამერუნი",
u"კანადა",
u"კატარი",
u"კენია",
u"კვიპროსი",
u"კინგმენის რიფი",
u"კირიბატი",
u"კლიპერტონი (კუნძული)",
u"ქოქოსის კუნძულები",
u"კოლუმბია",
u"კომორის კუნძულები",
u"კონგოს დემოკრატიული რესპუბლიკა",
u"კონგოს რესპუბლიკა",
u"კორეის რესპუბლიკა",
u"ჩრდილოეთი კორეა",
u"კოსტა-რიკა",
u"კოტ-დ’ივუარი",
u"კუბა",
u"კუკის კუნძულები",
u"ლაოსი",
u"ლატვია",
u"ლესოთო",
u"ლიბანი",
u"ლიბერია",
u"ლიბია",
u"ლიტვა",
u"ლიხტენშტაინი",
u"ლუქსემბურგი",
u"მადაგასკარი",
u"მავრიკი",
u"მავრიტანია",
u"მაიოტა",
u"მაკაო",
u"მაკედონია",
u"მალავი",
u"მალაიზია",
u"მალდივი",
u"მალი",
u"მალტა",
u"მაროკო",
u"მარშალის კუნძულები",
u"მარჯნის ზღვის კუნძულები",
u"მექსიკა",
u"მიანმარი",
u"მიკრონეზია",
u"მოზამბიკი",
u"მოლდოვა",
u"მონაკო",
u"მონსერატი",
u"მონტენეგრო",
u"მონღოლეთი",
u"ნამიბია",
u"ნაურუ",
u"ნეპალი",
u"ნიგერი",
u"ნიგერია",
u"ნიდერლანდი",
u"ნიდერლანდის ანტილები",
u"ნიკარაგუა",
u"ნიუე",
u"ნორვეგია",
u"ნორფოლკის კუნძული",
u"ომანი",
u"პაკისტანი",
u"პალაუ",
u"პალმირა (ატოლი)",
u"პანამა",
u"პაპუა-ახალი გვინეა",
u"პარაგვაი",
u"პერუ",
u"პიტკერნის კუნძულები",
u"პოლონეთი",
u"პორტუგალია",
u"პრინც-ედუარდის კუნძული",
u"პუერტო-რიკო",
u"ჟუან-დი-ნოვა",
u"რეუნიონი",
u"რუანდა",
u"რუმინეთი",
u"რუსეთი",
u"საბერძნეთი",
u"სალვადორი",
u"სამოა",
u"სამხრეთ აფრიკის რესპუბლიკა",
u"სამხრეთი გეორგია და სამხრეთ სენდვიჩის კუნძულები",
u"სამხრეთი სუდანი",
u"სან-მარინო",
u"სან-ტომე და პრინსიპი",
u"საუდის არაბეთი",
u"საფრანგეთი",
u"საფრანგეთის გვიანა",
u"საფრანგეთის პოლინეზია",
u"საფრანგეთის სამხრეთი პოლარული მიწები",
u"საქართველო",
u"სეიშელის კუნძულები",
u"სენეგალი",
u"სენ-პიერი და მიკელონი",
u"სენტ-ვინსენტი და გრენადინები",
u"სენტ-კიტსი და ნევისი",
u"სენტ-ლუსია",
u"სერბია და მონტენეგრო",
u"სეუტა",
u"სვაზილენდი",
u"სვალბარდი",
u"სიერა-ლეონე",
u"სინგაპური",
u"სირია",
u"სლოვაკეთი",
u"სლოვენია",
u"სოლომონის კუნძულები",
u"სომალი",
u"სომხეთი",
u"სუდანი",
u"სურინამი",
u"ტაივანი",
u"ტაილანდი",
u"ტანზანია",
u"ტაჯიკეთი",
u"ტორკსის და კაიკოსის კუნძულები",
u"ტოგო",
u"ტოკელაუ",
u"ტონგა",
u"ტრინიდადი და ტობაგო",
u"ტრომელინი (კუნძული)",
u"ტუვალუ",
u"ტუნისი",
u"უგანდა",
u"უზბეკეთი",
u"უკრაინა",
u"უნგრეთი",
u"ურუგვაი",
u"ფარერის კუნძულები",
u"ფილიპინები",
u"ფინეთი",
u"ფიჯი",
u"ფოლკლენდის კუნძულები",
u"ქუვეითი",
u"ღაზის სექტორი",
u"ყაზახეთი",
u"ყირგიზეთი",
u"შვეიცარია",
u"შვედეთი",
u"შობის კუნძული",
u"შრი-ლანკა",
u"ჩადი",
u"ჩეხეთი",
u"ჩილე",
u"ჩინეთი",
u"ჩრდილოეთი მარიანას კუნძულები",
u"ცენტრალური აფრიკის რესპუბლიკა",
u"წმინდა ელენეს კუნძული",
u"წყნარი ოკეანის კუნძულები",
u"ხორვატია",
u"ჯონსტრონი (ატოლი)",
u"ჯერვისი (კუნძული)",
u"ჯერსი",
u"ჯიბუტი",
u"ჰაიტი",
u"ჰონდურასი",
u"ჰონკონგი",
u"ჰოულენდი (კუნძული)",
u"ჰერდი და მაკდონალდის კუნძულები",
])

demonyms = set([
u"ავსტრალიელი",
u"ავსტრიელი",
u"ავღანელი",
u"აზერბაიჯანელი",
u"ალბანელი",
u"ალჟირელი",
u"სამოელი",
u"ვირჯინიელი",
u"ამერიკელი",
u"ანგლიელი",
u"ანგოლელი",
u"ანდორელი",
u"ანტიგუელი",
u"არაბი",
u"არგენტინელი",
u"არუბელი",
u"ტიმორელი",
u"ახალი ზელანდიელი",
u"კალედონიელი",
u"ბანგლადეშელი",
u"ბარბადოსელი",
u"ბაჰამელი",
u"ბაჰრეინელი",
u"ბელარუსი",
u"ბელგიელი",
u"ბელიზელი",
u"ბენინელი",
u"ბერმუდელი",
u"ბოლივიელი",
u"ბოსნიელი",
u"ბოსტვანელი",
u"ბრაზილიელი",
u"ბრუნეელი",
u"ბულგარელი",
u"ბურუნდიელი",
u"ბჰუტანელი",
u"გაბონელი",
u"გაიანაელი",
u"გამბიელი",
u"განელი",
u"გერმანელი",
u"გვადელუპელი",
u"გვატემალელი",
u"გვინეელი",
u"გიბრალტარელი",
u"გრენადელი",
u"გრენლანდიელი",
u"გუემელი",
u"დანიელი",
u"ინგლისელი",
u"დომინიკელი",
u"ეგვიპტელი",
u"ევროპელი",
u"ეთიოპიელი",
u"ეკვადორელი",
u"ერაყელი",
u"ერიტრიელი",
u"ესპანელი",
u"ესტონელი",
u"ვანუატუელი",
u"ვატიკანელი",
u"ვენესუელელი",
u"ვიეტნამელი",
u"ზამბიელი",
u"თურქი",
u"თურქმენი",
u"იამაიკელი",
u"იაპონელი",
u"იემენელი",
u"ინდოელი",
u"ინდონეზიელი",
u"იორდანიელი",
u"ირანელი",
u"ირლანდიელი",
u"ისლანდიელი",
u"ებრაელი",
u"იტალიელი",
u"კამბოჯელი",
u"კამერუნელი",
u"კანადელი",
u"კატარელი",
u"კენიელი",
u"კვიპროსელი",
u"კირიბატელი",
u"კოლუმბიელი",
u"კონგოელი",
u"კონგოელი",
u"კორეელი",
u"ჩრდილო კორეელი",
u"კოსტა–რიკელი",
u"კორტ–დივუარელი",
u"კუბელი",
u"ლაოსელი",
u"ლატვიელი",
u"ლიბანელი",
u"ლიბერიელი",
u"ლიბიელი",
u"ლიტველი",
u"ლუქსემბურგელი",
u"მავრიტანიელი",
u"მაკაოელი",
u"მაკედონიელი",
u"მალაველი",
u"მალაიზიელი",
u"მალდიველი",
u"მალტელი",
u"მაროკოელი",
u"მექსიკელი",
u"მიკრონეზიელი",
u"მოზამბიკელი",
u"მოლდოველი",
u"მონაკოელი",
u"მონტენეგროელი",
u"მონღოლი",
u"ნამიბიელი",
u"ნაურუელი",
u"ნეპალელი",
u"ნიგერიელი",
u"ჰოლანდიელი",
u"ნიკარაგუელი",
u"ნორვეგიელი",
u"ომანელი",
u"პაკისტანელი",
u"პალაუელი",
u"პალმიელი",
u"პანამელი",
u"პარაგვაელი",
u"პეუელი",
u"პოლონელი",
u"პორტუგალიელი",
u"პუერტო–რიკოელი",
u"რუანდელი",
u"რუმინელი",
u"რუსი",
u"ბერძენი",
u"სალვადორელი",
u"სამოელი",
u"აფრიკელი",
u"სამხრეთ სუდანელი",
u"სან–მარინოელი",
u"არაბი",
u"ფრანგი",
u"ქართველი",
u"სენეგალელი",
u"სენტ–ლუსიელი",
u"სერბი",
u"სვალბარდიელი",
u"სიერა–ლეონელი",
u"სინგაპურელი",
u"სირიელი",
u"სლოვაკი",
u"სლოვენიელი",
u"სომალელი",
u"სომეხი",
u"სუნდანელი",
u"სურინამელი",
u"ტაივანელი",
u"ტაილანდელი",
u"ტანზანიელი",
u"ტაჯიკი",
u"ტოგოელი",
u"ტოკელაუელი",
u"ტონგელი",
u"ტრინიდადელი",
u"ტრომელინელი",
u"ტუვალუელი",
u"ტუნისელი",
u"უგანდელი",
u"უზბეკი",
u"უკრაინელი",
u"უნგრელი",
u"ურუგვაელი",
u"ფილიპინელი",
u"ფინელი",
u"ქუვეითელი",
u"ღაზელი",
u"ყაზახი",
u"ყირგიზი",
u"შვიცარიელი",
u"შვედი",
u"შრი–ლანკელი",
u"ჩადელი",
u"ჩეხი",
u"ჩილელი",
u"ჩინელი",
u"ხორვატი",
u"ჯორსტრონელი",
u"ჯერვისელი",
u"ჯიბუტელი",
u"ჰაიტელი",
u"ჰონდურასელი",
u"ჰონკონგელი",
u"ჰოულენდელი",
])

