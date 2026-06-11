Pengembangan dan Evaluasi Model Hybrid Isolation Forest–Bayesian
Network untuk Deteksi Risiko Multi-Domain pada Rantai Pasok
Pertanian
PROPOSAL PENELITIAN
Diajukan untuk Memenuhi Salah Satu Syarat kelulusan Strata 1
di Program Studi Sistem Informasi Universitas Widyatama
Oleh
NAMA : Muhamad Surya Al Ghifari
NPM : 41121100003
PROGRAM STUDI SISTEM INFORMASI
FAKULTAS TEKNIK UNIVERSITAS WIDYATAMA
BANDUNG
2026

DAFTAR ISI
DAFTAR ISI ..................................................................................................................... ii
DAFTAR TABEL ............................................................................................................ iv
DAFTAR GAMBAR ........................................................................................................ v
BAB I PENDAHULUAN ................................................................................................. 1
1.1. Latar Belakang Masalah ..................................................................................... 1
1.2. Identifikasi dan Rumusan Masalah .................................................................... 3
1.3. Batasan Masalah ................................................................................................. 4
1.4. Tujuan Penelitian ............................................................................................... 4
1.5. Manfaat Penelitian ............................................................................................. 5
BAB II KAJIAN PUSTAKA ............................................................................................ 6
2.1. Tinjauan Teori .................................................................................................... 6
2.1.1. Anomaly Detection Pada Sistem Rantai Pasok ........................................... 6
2.1.2. Isolation Forest Dalam Deteksi Anomali ................................................... 7
2.1.3. Bayesian Network Untuk Pemodelan Risiko .............................................. 9
2.1.4. Model Hybrid Dalam Machine Learning ................................................. 11
2.1.5. Deteksi Risiko Multi-Domain Pada Sektor Pertanian ............................... 13
2.1.6. Sistem Peringatan Dini Berbasis AI .......................................................... 15
2.1.7. Ringkasan dan Posisi Penelitian ............................................................... 18
2.1.8. Kerangka Pemikiran ................................................................................. 21
2.2. Tinjauan Pustaka .............................................................................................. 22
2.2.1. Konsep Risiko dan Ketidakpastian ........................................................... 22
2.2.2. Rantai Pasok Pertanian dan Karakteristik Risikonya ............................... 23
2.2.3. Teori Anomaly Detection .......................................................................... 25
2.2.4. Teori Isolation Forest ............................................................................... 26
2.2.5. Teori Bayesian Network ............................................................................ 27
2.2.6. Naive Bayesian Network (Label Features) ............................................... 28
2.2.7. Model Hybrid Dalam Sistem Cerdas ........................................................ 30
2.2.8. Integrasi Skor dan Strategi Agregasi ........................................................ 31
2.2.9. Evaluasi Model Klasifikasi dan Deteksi Anomali .................................... 31
2.2.10. Penanganan Data Imbalance .................................................................... 33
BAB III METODOLOGI ................................................................................................ 35
3.1. Jenis Penelitian ................................................................................................. 35
ii

3.2. Metode Pengembangan Model ......................................................................... 36
3.3. Objek Penelitian ............................................................................................... 37
3.3.1. Domain Risiko Penelitian ......................................................................... 38
3.3.2. Entitas, Variabel, Satuan, dan Sumber Data ............................................. 43
3.3.3. Unit Analisis Penelitian ............................................................................ 46
3.4. Teknik Pengumpulan Data ............................................................................... 46
3.5. Teknik Analisis Data ........................................................................................ 47
3.5.1. Pembentukan Label Risiko ....................................................................... 47
3.5.2. Preprocessing dan Feature Engineering .................................................. 49
3.5.3. Pengembangan Model Isolation Forest .................................................... 52
3.5.4. Pengembangan Model Bayesian Network ................................................ 54
3.5.5. Pengembangan Model Hybrid Isolation Forest–Bayesian Network ........ 56
3.5.6. Mekanisme Threshold dan Keputusan Deteksi ........................................ 59
3.5.7. Evaluasi Model ......................................................................................... 62
3.5.8. Kalibrasi, Uncertainty, dan Explainability Model ................................... 64
3.6. Alur Penelitian ................................................................................................. 67
3.7. Jadwal Penelitian .............................................................................................. 70
DAFTAR PUSTAKA ..................................................................................................... 71
iii

DAFTAR TABEL
Tabel 2.1 Ringkasan Penelitian Terdahulu ..................................................................... 19
Tabel 2.1 (lanjutan) ......................................................................................................... 20
Tabel 3.1 Variabel, Satuan, dan Sumber Data per Domain ............................................ 43
Tabel 3.1 (lanjutan) ......................................................................................................... 44
Tabel 3.1 (lanjutan) ......................................................................................................... 45
Tabel 3.2 Strategi Temporal Alignment per Domain ...................................................... 51
Tabel 3.3 Jadwal Penelitian ........................................................................................... 70
iv

DAFTAR GAMBAR
Gambar 2.1 Kerangka Pemikiran .................................................................................... 22
Gambar 3.1 Pipeline Pengembangan Model .................................................................. 36
Gambar 3.2 Alur Pengembangan Model Hybrid ............................................................ 57
Gambar 3.3 Alur Penelitian ............................................................................................ 67
v

BAB I
PENDAHULUAN
1.1. Latar Belakang Masalah
Rantai pasok pertanian menghadapi tekanan yang semakin kompleks akibat
keterkaitan antara faktor ekonomi, lingkungan, dan operasional yang terus berkembang.
Gangguan pada satu titik dalam sistem, seperti guncangan harga komoditas, anomali
cuaca, atau hambatan distribusi, dapat merambat dan memperburuk kondisi pada titik
lainnya secara bersamaan [1], [2]. Bukti empiris menunjukkan bahwa variasi cuaca
mampu menjelaskan lebih dari separuh variasi hasil pertanian dan berdampak lanjutan
pada pendapatan petani serta stabilitas kredit [3]. Di sisi lain, dinamika harga komoditas
juga dipengaruhi secara simultan oleh faktor energi, iklim, dan interaksi pasar. Kondisi
tersebut menunjukkan bahwa risiko pada rantai pasok pertanian tidak dapat dipahami
hanya dari satu domain, melainkan terbentuk dari interaksi beberapa lapisan risiko dengan
karakteristik yang berbeda. Oleh karena itu, diperlukan pendekatan deteksi yang mampu
memantau beberapa domain secara bersamaan sebagai dasar sistem peringatan dini yang
lebih terstruktur [1]–[3].
Berbagai penelitian mengenai deteksi anomali dan pemodelan risiko pada sektor
pertanian menunjukkan potensi yang cukup besar, tetapi sebagian besar masih dilakukan
secara parsial, misalnya hanya berfokus pada domain harga, cuaca, atau organisme
pengganggu tanaman [4]–[7], [3], [8]. Selain itu, pendekatan yang digunakan umumnya
masih bertumpu pada model tunggal yang memiliki keterbatasan masing-masing.
Isolation Forest unggul dalam mendeteksi penyimpangan secara unsupervised dan efisien
pada data multivariat, tetapi terbatas dalam memberikan interpretasi probabilistik [10]–
[12]. Sebaliknya, Bayesian Network kuat dalam pemodelan risiko probabilistik dan
inferensi di bawah ketidakpastian, tetapi menghadapi tantangan pada data kontinu
berskala besar, pembentukan struktur model, dan heterogenitas data [9], [12], [13].
Perbedaan karakteristik tersebut menunjukkan bahwa kedua metode memiliki potensi
yang saling melengkapi. Isolation Forest dapat menangkap sinyal penyimpangan tanpa
bergantung pada label, sedangkan Bayesian Network dapat memperkuat keputusan
deteksi melalui inferensi probabilistik berbasis label operasional [14], [15]. Meskipun
demikian, integrasi eksplisit antara kedua metode tersebut dalam satu kerangka deteksi
risiko multi-domain pada rantai pasok pertanian masih relatif terbatas.
1

2
Kebutuhan akan pendekatan yang menghubungkan deteksi anomali dengan
inferensi probabilistik dalam satu kerangka multi-domain masih menjadi celah penelitian
yang belum banyak dieksplorasi. Model hybrid yang mengintegrasikan Isolation Forest
dan Bayesian Network berpotensi memanfaatkan keunggulan kedua metode secara
bersama-sama, sehingga hasil deteksi tidak hanya mampu mengidentifikasi
penyimpangan, tetapi juga memberikan dasar penalaran risiko yang lebih terstruktur
[14]–[16]. Di sisi lain, pendekatan per-domain tetap diperlukan agar perbedaan
karakteristik data pada setiap domain dapat ditangani secara lebih sesuai, baik dalam
pembentukan fitur, pembentukan label, maupun mekanisme deteksi. Dengan demikian,
integrasi model hybrid dan pemodelan per-domain merupakan dua kebutuhan
metodologis yang saling berkaitan dalam pengembangan sistem deteksi risiko multi-
domain.
Berdasarkan keterbatasan pendekatan yang ada dan kebutuhan akan deteksi risiko
multi-domain yang lebih terstruktur, penelitian ini mengembangkan dan mengevaluasi
model hybrid Isolation Forest–Bayesian Network untuk deteksi risiko multi-domain pada
rantai pasok pertanian. Model dikembangkan secara per-domain untuk menangani
perbedaan karakteristik data pada enam domain risiko, yaitu harga, cuaca, organisme
pengganggu tanaman (OPT), distribusi, tindakan pengelolaan, dan produksi. Pemodelan
dilakukan dengan resolusi mingguan per kecamatan di Kabupaten Sumedang,
menggunakan data historis periode 2022–2024, agar pola musiman dan tren multi-tahun
pada masing-masing domain risiko dapat direpresentasikan secara memadai. Evaluasi
dilakukan dengan membandingkan performa model Isolation Forest, Bayesian Network,
dan model hybrid dalam menghasilkan probabilitas risiko dan keputusan deteksi, sebagai
dasar pengembangan sistem peringatan dini pada rantai pasok pertanian. Dengan
demikian, penelitian ini diharapkan memberikan kontribusi metodologis terhadap
pengembangan pendekatan deteksi risiko yang lebih terstruktur dan relevan untuk sektor
pertanian.

3
1.2. Identifikasi dan Rumusan Masalah
a) Identifikasi Masalah
Berdasarkan latar belakang yang telah diuraikan, dapat diidentifikasi beberapa
masalah sebagai berikut:
(1) Risiko pada rantai pasok pertanian bersifat multi-domain dan memiliki
karakteristik yang berbeda pada setiap domain, sehingga tidak mudah
dideteksi dengan pendekatan tunggal.
(2) Pendekatan deteksi risiko pada sektor pertanian masih cenderung
dilakukan secara parsial, misalnya hanya pada domain harga, cuaca, atau
organisme pengganggu tanaman.
(3) Isolation Forest dan Bayesian Network memiliki keunggulan yang
berbeda dalam deteksi risiko, namun belum banyak diintegrasikan secara
eksplisit dalam satu model untuk deteksi risiko multi-domain pada rantai
pasok pertanian.
(4) Diperlukan evaluasi untuk membandingkan performa model tunggal dan
model hybrid dalam mendeteksi risiko pada data penelitian.
b) Rumusan Masalah
Berdasarkan identifikasi masalah tersebut, maka rumusan masalah dalam
penelitian ini adalah sebagai berikut:
(1) Bagaimana mengembangkan model hybrid Isolation Forest-Bayesian
Network untuk deteksi risiko multi-domain pada rantai pasok pertanian?
(2) Bagaimana performa Isolation Forest, Bayesian Network, dan model
hybrid Isolation Forest-Bayesian Network dalam mendeteksi risiko pada
masing-masing domain dalam rantai pasok pertanian?
(3) Bagaimana hasil perbandingan performa antara Isolation Forest, Bayesian
Network, dan model hybrid Isolation Forest-Bayesian Network dalam
menghasilkan skor risiko dan keputusan deteksi pada data penelitian?

4
1.3. Batasan Masalah
Batasan masalah dalam penelitian ini ditetapkan agar ruang lingkup penelitian
tetap terarah dan sesuai dengan tujuan yang telah ditetapkan. Batasan-batasan masalah
dalam penelitian ini adalah sebagai berikut:
a) Penelitian difokuskan pada pengembangan dan evaluasi model hybrid Isolation
Forest–Bayesian Network untuk deteksi risiko multi-domain pada rantai pasok
pertanian. Keluaran model berupa probabilitas risiko, keputusan deteksi anomali,
dan tingkat keparahan per domain dirancang agar dapat diintegrasikan ke dalam
sistem peringatan dini, namun implementasi sistem secara operasional berada di
luar cakupan penelitian ini.
b) Data yang digunakan merupakan data historis periode 2022–2024 pada wilayah
Kabupaten Sumedang.
c) Domain risiko yang dianalisis mencakup enam domain, yaitu harga, cuaca,
organisme pengganggu tanaman (OPT), distribusi, tindakan pengelolaan, dan
produksi.
d) Evaluasi penelitian difokuskan pada keluaran model berupa skor risiko dan
keputusan deteksi terhadap label operasional yang telah dibentuk, sehingga tidak
mencakup evaluasi terhadap alert operasional secara menyeluruh.
1.4. Tujuan Penelitian
Berdasarkan rumusan masalah yang telah ditetapkan, maka tujuan penelitian ini
adalah sebagai berikut:
a) Mengembangkan model hybrid Isolation Forest-Bayesian Network untuk deteksi
risiko multi-domain pada rantai pasok pertanian.
b) Mengevaluasi performa Isolation Forest, Bayesian Network, dan model hybrid
Isolation Forest-Bayesian Network dalam mendeteksi risiko pada masing-masing
domain dalam rantai pasok pertanian.
c) Menganalisis hasil perbandingan performa antara Isolation Forest, Bayesian
Network, dan model hybrid Isolation Forest-Bayesian Network dalam
menghasilkan skor risiko dan keputusan deteksi pada data penelitian.

5
1.5. Manfaat Penelitian
a) Manfaat Teoritis
(1) Memberikan kontribusi pada pengembangan kajian mengenai integrasi
metode anomaly detection dan probabilistic reasoning dalam deteksi
risiko multi-domain pada rantai pasok pertanian.
(2) Menambah referensi akademik mengenai penerapan model hybrid
Isolation Forest–Bayesian Network dalam deteksi risiko berbasis data.
(3) Memperkaya pemahaman tentang penggunaan pendekatan per-domain
dalam pemodelan risiko pertanian yang memiliki karakteristik data dan
distribusi yang berbeda.
b) Manfaat Praktis
(1) Memberikan dasar pengembangan sistem deteksi risiko yang lebih
terstruktur untuk memantau berbagai domain risiko pada rantai pasok
pertanian.
(2) Menghasilkan keluaran model berupa probabilitas risiko, keputusan
deteksi anomali, dan tingkat keparahan (severity) per domain yang dapat
dimanfaatkan sebagai dasar pengembangan sistem peringatan dini pada
rantai pasok pertanian.
(3) Menjadi referensi bagi peneliti atau pengembang sistem yang ingin
menerapkan pendekatan hybrid pada data risiko pertanian atau data multi-
domain sejenis.

BAB II
KAJIAN PUSTAKA
2.1. Tinjauan Teori
2.1.1. Anomaly Detection Pada Sistem Rantai Pasok
Penelitian mengenai anomaly detection pada sistem rantai pasok
menunjukkan bahwa anomali tidak hanya muncul pada aktivitas distribusi barang,
tetapi juga pada struktur hubungan antarentitas, pergerakan logistik, dinamika harga
komoditas, hingga proses produksi pertanian. Seiring dengan semakin beragamnya
bentuk data yang digunakan, mulai dari graf jaringan, data sensor real-time, deret
waktu harga, hingga data multimodal pertanian, pendekatan deteksi anomali yang
diterapkan juga berkembang menjadi semakin kompleks. Hal ini menunjukkan
bahwa deteksi anomali merupakan bagian penting dalam mengidentifikasi gangguan,
penyimpangan, dan risiko yang dapat memengaruhi kinerja rantai pasok secara
keseluruhan [4]–[7].
Pada struktur jaringan rantai pasok, anomali dapat dipahami sebagai
penyimpangan hubungan antar-node dalam jaringan pengadaan. Pendekatan berbasis
graf melalui Graph Balancing Theory, Laplacian flow, dan Sheaf theory digunakan
untuk mengidentifikasi entitas yang menunjukkan inkonsistensi struktural dalam
jaringan supply chain [4]. Temuan tersebut menunjukkan bahwa anomali pada rantai
pasok tidak selalu termanifestasi sebagai gangguan operasional yang tampak secara
langsung, tetapi juga dapat berbentuk distorsi informasi serta ketidakwajaran pola
relasi antarpelaku dalam jaringan [4].
Pada distribusi logistik, anomali umumnya muncul pada aliran data sensor
yang dipantau secara real-time, seperti suhu, kelembapan, oksigen, karbon dioksida,
dan tekanan pada logistik rantai dingin [5]. Untuk mendeteksi penyimpangan
tersebut, digunakan improved Isolation Forest yang terbukti memberikan kinerja
lebih baik dibandingkan Support Vector Machine (SVM), Local Outlier Factor
(LOF), dan Isolation Forest standar [5]. Temuan ini mengindikasikan bahwa metode
deteksi anomali pada distribusi logistik perlu mampu menangani data streaming
multivariat dengan ketergantungan temporal yang kuat [5].
6

7
Selain pada jaringan dan distribusi, deteksi anomali juga diterapkan pada
harga komoditas dan produksi pertanian. Pada harga komoditas, anomali dideteksi
melalui kombinasi Transformer dan attention-boosted LSTM-VAE untuk mengenali
perubahan harga yang tidak wajar pada deret waktu harian [6]. Sementara itu, pada
produksi pertanian, anomali muncul dalam bentuk gangguan kesehatan tanaman,
seperti serangan hama, penyakit, defisiensi nutrisi, dan stres lingkungan. Untuk
menangani kondisi tersebut, digunakan pendekatan deep learning multimodal yang
memadukan multi-modal fusion, Graph Neural Network (GNN), Transformer, dan
Variational Autoencoder (VAE) agar berbagai sumber data dapat dianalisis secara
terpadu [7]. Kedua penelitian tersebut menunjukkan bahwa data harga dan produksi
menuntut metode yang lebih kompleks karena pola yang diamati bersifat dinamis,
heterogen, serta memiliki keterkaitan temporal dan spasial [6], [7].
Berdasarkan penelitian-penelitian tersebut, dapat disimpulkan bahwa
anomaly detection pada sistem rantai pasok telah diterapkan pada berbagai aspek,
mulai dari struktur jaringan supply chain, distribusi logistik, harga komoditas, hingga
produksi pertanian [4]–[7]. Setiap penelitian menggunakan pendekatan yang berbeda
sesuai dengan karakteristik data dan objek anomali yang dianalisis. Namun, sebagian
besar penelitian masih berfokus pada satu domain tertentu, sehingga hasil deteksi
cenderung bersifat parsial dan belum sepenuhnya menggambarkan keterkaitan
antarsumber risiko dalam rantai pasok pertanian secara menyeluruh. Dengan
demikian, penelitian mengenai anomaly detection pada sistem rantai pasok masih
menunjukkan kebutuhan akan pengembangan pendekatan yang lebih terintegrasi
[4]–[7].
2.1.2. Isolation Forest Dalam Deteksi Anomali
Isolation Forest merupakan salah satu metode anomaly detection berbasis
isolation yang dikembangkan dengan asumsi bahwa data anomali cenderung lebih
mudah dipisahkan dibandingkan data normal. Berbeda dengan pendekatan yang
bergantung pada estimasi densitas atau perhitungan jarak antar titik data, Isolation
Forest membangun sekumpulan pohon acak untuk mengisolasi observasi melalui
proses partisi berulang. Semakin pendek jalur isolasi suatu data, semakin besar
kemungkinan data tersebut merupakan anomali. Karakteristik ini menjadikan
Isolation Forest banyak digunakan dalam penelitian deteksi anomali karena mampu

8
bekerja tanpa data berlabel, relatif efisien secara komputasi, dan dapat diterapkan
pada berbagai bentuk data multivariat [17]–[20].
Dalam penelitian terdahulu, Isolation Forest telah diterapkan pada berbagai
konteks deteksi anomali, terutama pada sistem monitoring dan data operasional
multivariat. Pada konteks software-defined networking (SDN), metode ini digunakan
untuk mendeteksi anomali lalu lintas jaringan dan dihubungkan dengan decision
engine, alert system, serta pembaruan kebijakan secara adaptif [17]. Pada penelitian
lain, Isolation Forest diterapkan untuk mendeteksi aplikasi mobile yang
mencurigakan berdasarkan pola permission request dalam bentuk fitur biner
berdimensi tinggi [18]. Selain itu, dalam konteks process quality control, Isolation
Forest juga digunakan sebagai novelty detector untuk memantau proses multivariat
non-normal dan dibandingkan dengan pendekatan statistik klasik seperti Hotelling’s
T² [20]. Ragam penerapan tersebut menunjukkan bahwa Isolation Forest tidak
terbatas pada satu domain tertentu, tetapi cukup fleksibel untuk digunakan pada data
yang memiliki struktur, distribusi, dan tujuan pemantauan yang berbeda.
Salah satu alasan utama banyaknya penggunaan Isolation Forest adalah
kemampuannya menangani data multivariat dan berdimensi tinggi secara relatif
efisien. Pada deteksi aplikasi mobile, Isolation Forest dinilai sesuai untuk data
permission request yang terdiri atas banyak fitur biner dan bersifat tidak seimbang,
terutama setelah dilakukan parameter tuning yang tepat [18]. Penelitian tersebut
menunjukkan bahwa pengaturan parameter yang baik mampu menurunkan false
positive secara signifikan serta meningkatkan precision, sehingga memperlihatkan
bahwa keandalan Isolation Forest tidak hanya terletak pada algoritmanya, tetapi juga
pada konfigurasi model yang digunakan [18]. Di sisi lain, penelitian pada process
quality control menunjukkan bahwa Isolation Forest memiliki keunggulan pada data
multivariat non-Gaussian, karena tidak bergantung pada asumsi distribusi tertentu
sebagaimana pendekatan berbasis kovarians [20]. Dengan demikian, Isolation Forest
dapat dipandang sebagai metode yang cukup kuat untuk mendeteksi penyimpangan
pada data kompleks yang sulit ditangani oleh metode statistik konvensional.

9
Meskipun memiliki keunggulan tersebut, Isolation Forest memiliki dua
keterbatasan penting. Pertama, sensitivitas terhadap contamination rate yang
berpengaruh langsung terhadap ambang keputusan dan jumlah anomali yang
dihasilkan [17],[18]. Pada konteks SDN, peningkatan contamination berkorelasi
dengan bertambahnya alert dan perubahan kebijakan, sehingga muncul trade-off
antara sensitivitas deteksi dan stabilitas operasional [17]. Pada deteksi aplikasi
mobile, contamination juga menjadi hyperparameter penentu keseimbangan antara
peningkatan deteksi dan risiko false positive [18]. Kedua, keterbatasan
interpretabilitas. Keluaran Isolation Forest berupa skor anomali tidak secara
langsung menjelaskan mengapa suatu observasi dianggap abnormal. Keterbatasan ini
mendorong pengembangan seperti CADI yang membedakan local dan global
anomaly berdasarkan struktur inlier [19]. Selain itu, Isolation Forest memiliki
sensitivitas rendah terhadap perubahan halus seperti small mean shift [20]. Temuan-
temuan ini menunjukkan bahwa kekuatan Isolation Forest dalam efisiensi dan
fleksibilitas belum sepenuhnya diikuti oleh kemampuan penjelasan dan pemodelan
hubungan antar variabel.
2.1.3. Bayesian Network Untuk Pemodelan Risiko
Bayesian Network merupakan salah satu pendekatan probabilistik yang
banyak digunakan dalam pemodelan risiko karena mampu merepresentasikan
hubungan ketergantungan antar variabel dalam bentuk directed acyclic graph
(DAG). Melalui struktur tersebut, Bayesian Network tidak hanya digunakan untuk
menghitung probabilitas suatu kejadian, tetapi juga untuk melakukan probabilistic
reasoning, diagnostic inference, predictive inference, dan analisis ketidakpastian
secara lebih terstruktur. Karakteristik ini menjadikan Bayesian Network relevan
dalam berbagai kebutuhan pengambilan keputusan di bawah kondisi tidak pasti,
terutama ketika hubungan antar faktor risiko perlu dipahami secara eksplisit [9]–[12].
Dalam penelitian terdahulu, Bayesian Network telah diterapkan pada
berbagai bidang pemodelan risiko, mulai dari lingkungan industri, prediksi risiko
klinis, hingga sistem monitoring pada infrastruktur [9], [10], [12]. Pada skala industri
besar, Bayesian Network digunakan untuk memodelkan dependensi antar variabel
risiko, menangani data yang tidak lengkap, serta mendukung inferensi diagnostik,
prognostik, dan counterfactual reasoning dalam pengambilan keputusan operasional

10
[9]. Sementara itu, pada structural health monitoring, Bayesian Network
dimanfaatkan untuk mengintegrasikan data multi-sensor, memperbarui keyakinan
ketika data baru masuk, serta mendukung early warning dan strategi pemeliharaan
[12]. Temuan-temuan ini menunjukkan bahwa kekuatan utama Bayesian Network
terletak pada kemampuannya menghubungkan berbagai sumber informasi dalam satu
kerangka probabilistik yang koheren [9], [12].
Selain digunakan sebagai alat probabilistic reasoning, pendekatan Bayesian
juga berkembang dalam bentuk yang lebih sederhana, yaitu Naive Bayes, untuk
keperluan klasifikasi risiko. Pada penelitian di bidang penilaian risiko kredit, Naive
Bayes digunakan untuk mengklasifikasikan kelayakan kredit berdasarkan sejumlah
atribut keuangan dan karakteristik pemohon [11]. Model ini menunjukkan bahwa
pendekatan Bayesian tetap efektif digunakan pada tugas klasifikasi probabilistik
karena memiliki struktur yang sederhana, cepat, dan dapat bekerja dengan data latih
yang terbatas [11]. Namun, berbeda dengan Bayesian Network penuh, Naive Bayes
tidak memodelkan relasi kompleks antar fitur karena bergantung pada asumsi
independensi kondisional terhadap kelas. Oleh karena itu, Naive Bayes dapat
dipahami sebagai bentuk pendekatan Bayesian yang berguna untuk klasifikasi risiko
sederhana, tetapi kurang memadai ketika hubungan antar variabel risiko perlu
direpresentasikan secara eksplisit [11].
Penelitian lain menunjukkan bahwa efektivitas Bayesian Network sangat
dipengaruhi oleh kualitas struktur DAG yang digunakan. Pada studi prediksi late
morbidity, struktur Bayesian Network dioptimalkan menggunakan simulated
annealing karena struktur bawaan yang dihasilkan secara otomatis belum tentu logis
atau sesuai dengan hubungan kausal yang diharapkan [10]. Temuan ini menegaskan
bahwa Bayesian Network memiliki kekuatan pada kemampuan representasi
dependensi, tetapi sekaligus sangat bergantung pada bagaimana struktur hubungan
antar variabel dibangun [10]. Jika struktur DAG yang dihasilkan kurang tepat, maka
kualitas inferensi, interpretabilitas, dan relevansi hasil keputusan juga dapat
menurun. Dengan demikian, keunggulan Bayesian Network dalam probabilistic
modeling tidak dapat dipisahkan dari tantangan dalam proses structure learning serta
kebutuhan akan pengetahuan pakar untuk membatasi atau memvalidasi arah
hubungan antarnode [9], [10].

11
Bayesian Network juga menghadapi keterbatasan pada data kontinu besar dan
sistem berdimensi tinggi. Pada data industri muncul tantangan heterogenitas data dan
kompleksitas struktur [9] pada studi klinis variabel kontinu perlu didiskretisasi
terlebih dahulu [10] sedangkan pada structural health monitoring muncul curse of
dimensionality dan kompleksitas komputasi pada sistem dinamis berskala besar [12].
Berdasarkan berbagai penelitian tersebut, Bayesian Network merupakan metode
yang kuat untuk probabilistic reasoning dan pemodelan risiko karena mampu
merepresentasikan ketergantungan antar variabel [9]–[12], tetapi belum cukup
apabila digunakan sendiri untuk membangun sistem deteksi risiko yang menuntut
kemampuan identifikasi anomali sekaligus penalaran probabilistik secara terpadu.
Kondisi ini menegaskan perlunya pendekatan pelengkap yang menghubungkan
kekuatan deteksi anomali dengan kemampuan pemodelan risiko dalam satu
kerangka.
2.1.4. Model Hybrid Dalam Machine Learning
Perkembangan penelitian machine learning menunjukkan bahwa
penggunaan model tunggal sering kali belum cukup untuk menangani data anomali
yang kompleks, terutama ketika pola penyimpangan bersifat heterogen, dinamis, dan
dipengaruhi oleh banyak faktor sekaligus. Oleh karena itu, berbagai penelitian mulai
mengembangkan pendekatan hybrid dengan menggabungkan beberapa model agar
dapat memanfaatkan keunggulan masing-masing komponen. Dalam penelitian
anomaly detection, pendekatan ini digunakan untuk meningkatkan sensitivitas
deteksi, memperbaiki stabilitas hasil, dan mengurangi kelemahan yang muncul
apabila hanya satu model digunakan secara mandiri [14], [15], [16], [21], [22].
Sejumlah penelitian memperlihatkan bahwa hybrid anomaly detection dapat
dibangun melalui penggabungan model supervised dan unsupervised. Pada deteksi
fraud kartu kredit, kerangka XRAI mengintegrasikan XGBoost, Random Forest,
Autoencoder, dan Isolation Forest dalam satu sistem heterogeneous weighted
ensemble [14]. Integrasi dilakukan melalui normalisasi skor masing-masing model
ke rentang yang sama, kemudian digabungkan dengan weighted sum dan
thresholding untuk menghasilkan keputusan akhir [14]. Strategi ini menunjukkan
bentuk score-level fusion, yaitu penggabungan keluaran model pada level skor,
bukan pada level fitur atau representasi. Hasil penelitian menunjukkan bahwa

12
pendekatan tersebut mampu memberikan recall, precision, dan F1-score yang lebih
baik dibandingkan beberapa model pembanding, meskipun tetap menghadapi isu
kompleksitas model dan tingginya false positive dari beberapa komponen tertentu
[14]. Temuan ini menunjukkan bahwa pendekatan hybrid dapat meningkatkan
performa deteksi, tetapi kualitas hasil tetap bergantung pada cara skor dari masing-
masing model digabungkan.
Selain penggabungan skor antarmodel, penelitian lain menunjukkan bahwa
integrasi hybrid juga dapat dilakukan melalui kombinasi antara komponen
unsupervised dan inferensi probabilistik. Pada sistem monitoring pompa pendingin
reaktor nuklir, pendekatan Kernel Self-Organizing Map dipadukan dengan Bayesian
Posterior Inference untuk membangun mekanisme deteksi anomali yang lebih dapat
ditelusuri [15]. Dalam pendekatan ini, Kernel SOM digunakan untuk memodelkan
pola normal secara unsupervised, sedangkan distribusi probabilitas jarak antar cluster
dimanfaatkan untuk menghitung probabilitas posterior keadaan normal [15].
Integrasi semacam ini tidak sepenuhnya berada pada score-level fusion klasik
maupun feature-level fusion, melainkan lebih mendekati penggabungan representasi
lokal dengan mekanisme penalaran probabilistik. Penelitian lain pada structural
health monitoring juga menunjukkan pola serupa, yaitu memanfaatkan manifold
learning-aided data clustering dan non-parametric probabilistic anomaly detection
untuk membangun anomaly score berdasarkan subset lokal data [21]. Kedua
penelitian tersebut menunjukkan bahwa model unsupervised dapat dipadukan dengan
komponen probabilistik untuk meningkatkan reliabilitas deteksi, terutama pada data
yang dipengaruhi variasi lingkungan dan pola lokal yang kompleks [15], [21].
Perbedaan strategi integrasi juga terlihat pada penelitian yang menekankan
decision-level maupun feature-level fusion. Pada deteksi anomali kapsul endoskopi,
beberapa base learner berupa autoencoder, autoencoder dengan classification head,
dan image classifier digabungkan melalui meta-classifier Random Forest atau SVM
VM [22]. Pendekatan ini memperlihatkan bentuk decision-level fusion, karena
prediksi dari model tingkat bawah dipelajari kembali untuk menghasilkan keputusan
akhir [22]. Sementara itu, pada sistem Industrial Control Systems (ICS), integrasi
dilakukan melalui dua tahap, yaitu feature augmentation dan weighted score
aggregation [16]. Skor anomali dari Autoencoder dan Isolation Forest terlebih

13
dahulu digunakan sebagai fitur tambahan bagi XGBoost dan Random Forest,
kemudian skor dari seluruh komponen diagregasi kembali untuk menghasilkan
keputusan akhir [16]. Dengan demikian, penelitian ini memperlihatkan bahwa
pendekatan hybrid tidak hanya dilakukan pada level skor, tetapi juga dapat dibangun
pada level fitur. Perbedaan ini penting karena score-level fusion cenderung lebih
sederhana dan fleksibel, sedangkan feature-level fusion berpotensi menangkap
hubungan antarkomponen secara lebih kaya, meskipun dengan kompleksitas
integrasi yang lebih tinggi [14], [16], [22].
Berdasarkan berbagai penelitian tersebut, model hybrid dalam machine
learning telah dikembangkan melalui strategi integrasi yang beragam, yaitu score-
level fusion, decision-level fusion, feature-level fusion, dan penggabungan
representasi lokal dengan probabilistic inference [14], [16], [21], [22]. Sebagian
besar penelitian masih berfokus pada penggabungan model untuk meningkatkan
akurasi deteksi, dan integrasi yang secara eksplisit memanfaatkan Isolation Forest
dan Bayesian Network dalam satu arsitektur terpadu masih terbatas. Kondisi ini
menyisakan celah penting yang menjadi fokus penelitian ini, yaitu pengembangan
model hybrid berbasis feature-level fusion yang menghubungkan keunggulan deteksi
anomali Isolation Forest dengan kemampuan penalaran risiko Bayesian Network.
2.1.5. Deteksi Risiko Multi-Domain Pada Sektor Pertanian
Penelitian mengenai risiko pada sektor pertanian menunjukkan bahwa
sumber ketidakpastian dalam sistem pertanian tidak hanya berasal dari satu faktor,
tetapi terbentuk dari berbagai layer yang saling memengaruhi, seperti risiko harga,
risiko cuaca, risiko organisme pengganggu tanaman (OPT), risiko distribusi, risiko
tindakan pengelolaan, dan risiko produksi. Meskipun demikian, sebagian besar
penelitian terdahulu masih memodelkan risiko tersebut secara terpisah sesuai fokus
domain masing-masing. Akibatnya, pemahaman yang dihasilkan sering kali terbatas
pada satu jenis gangguan tertentu dan belum sepenuhnya menggambarkan hubungan
antar-layer risiko dalam sistem pertanian secara menyeluruh [3], [8], [23], [24].
Pada risiko harga, penelitian umumnya menempatkan volatilitas harga
komoditas sebagai bentuk utama ketidakpastian yang memengaruhi keberlanjutan
usaha pertanian. Salah satu studi menunjukkan bahwa kondisi meteorologis
berpengaruh kuat terhadap volatilitas harga komoditas, sehingga integrasi data iklim

14
mampu meningkatkan prediksi volatilitas dan perancangan mekanisme lindung nilai
seperti minimum support price dan skema asuransi [23]. Meskipun penelitian
tersebut telah menghubungkan harga dengan cuaca dan instrumen keuangan,
integrasi yang dilakukan masih berpusat pada layer ekonomi-finansial dan belum
menghubungkannya dengan risiko biologis seperti OPT maupun risiko distribusi
secara operasional [23]. Hal ini menunjukkan bahwa pada domain harga, perluasan
variabel telah mulai dilakukan, tetapi belum berkembang menjadi pemodelan risiko
pertanian yang benar-benar lintas layer.
Pada risiko OPT, penelitian terdahulu banyak memanfaatkan early warning
system berbasis prakiraan cuaca untuk memperkirakan potensi wabah penyakit atau
gangguan tanaman. Studi pada penyakit wheat blast menunjukkan bahwa suhu, curah
hujan, kelembapan relatif, dan variabel lingkungan lain dapat digunakan untuk
membangun sistem peringatan dini yang tervalidasi dan diadopsi secara luas oleh
pengguna lapangan [8]. Temuan ini memperlihatkan bahwa risiko OPT telah
dimodelkan secara cukup baik dengan menghubungkan faktor biologis dan cuaca.
Namun, integrasi tersebut tetap terbatas pada hubungan antara penyakit dan faktor
lingkungan, tanpa menghubungkannya lebih lanjut dengan dampak terhadap harga,
distribusi, atau keputusan rantai pasok secara lebih luas [8]. Dengan demikian, studi
pada domain OPT masih menunjukkan kecenderungan untuk berhenti pada layer
biologis dan agroklimat, bukan pada integrasi risiko pertanian yang menyeluruh.
Pada risiko distribusi, penelitian banyak berfokus pada gangguan logistik dan
pascapanen, terutama pada sistem rantai dingin untuk komoditas yang mudah rusak.
Studi mengenai ekspor durian dari Thailand ke China mengidentifikasi 16 faktor
risiko pada rantai dingin, mulai dari kekurangan pasokan, kekurangan kontainer,
kerusakan alat pengendali suhu, hingga persoalan sertifikasi [24]. Penelitian ini
memperlihatkan bahwa distribusi pertanian memiliki kerentanan yang nyata dan
dapat dianalisis sebagai domain risiko tersendiri. Namun, walaupun mencakup
beberapa jenis risiko operasional dan pasokan, penelitian tersebut belum
menghubungkannya secara langsung dengan risiko harga, cuaca, maupun OPT dalam
satu model terpadu [24]. Hal ini menunjukkan bahwa pada layer distribusi, penelitian
masih dominan menilai risiko logistik secara spesifik dan belum menempatkannya
sebagai bagian dari sistem risiko pertanian yang saling terhubung.

15
Sementara itu, pada risiko cuaca, penelitian menunjukkan bahwa variabilitas
dan kejutan iklim dapat memengaruhi hasil produksi, pendapatan petani, hingga
risiko gagal bayar kredit. Studi empiris di Brazil menunjukkan bahwa komponen
iklim seperti tren, musim, covariate shocks, dan idiosyncratic shocks dapat
menjelaskan lebih dari separuh variasi hasil, serta berimplikasi pada peningkatan
volatilitas pendapatan dan risiko kredit di masa depan [3]. Temuan ini menegaskan
bahwa risiko cuaca tidak hanya berdampak pada produksi, tetapi juga menjalar ke
aspek ekonomi pertanian. Meskipun demikian, integrasi yang dibangun masih
berpusat pada rantai cuaca-produksi-pendapatan-kredit, dan belum menyatukan
secara langsung risiko harga, OPT, dan distribusi dalam satu kerangka yang sama [3]
Berdasarkan berbagai penelitian tersebut, dapat dilihat bahwa risiko pada
sektor pertanian memang telah dimodelkan pada berbagai domain, tetapi sebagian
besar masih dilakukan secara terpisah atau hanya menghubungkan dua sampai tiga
layer risiko secara terbatas [3], [8], [23]. Risiko harga cenderung dikaitkan dengan
cuaca dan instrumen keuangan [23], risiko OPT banyak dipadukan dengan faktor
agroklimat untuk early warning [8], risiko distribusi dianalisis pada level logistik dan
pascapanen [24], sedangkan risiko cuaca sering diperluas hingga dampaknya pada
produksi dan pendapatan [3]. Namun, belum banyak penelitian yang menyatukan
domain harga, cuaca, OPT, distribusi, tindakan pengelolaan, dan produksi secara
simultan dalam satu kerangka deteksi risiko pertanian. Kondisi ini menunjukkan
bahwa penelitian pada sektor pertanian masih menyisakan kebutuhan akan
pendekatan multi-domain yang mampu memodelkan keterkaitan antar-layer risiko
secara lebih terpadu dan operasional.
2.1.6. Sistem Peringatan Dini Berbasis AI
Penelitian mengenai sistem peringatan dini berbasis AI menunjukkan bahwa
peran model prediktif tidak berhenti pada proses deteksi atau klasifikasi, tetapi
berlanjut pada pembentukan mekanisme peringatan yang dapat digunakan untuk
mendukung keputusan operasional. Dalam berbagai studi, sistem peringatan dini
dibangun dengan pola umum berupa pengumpulan data multivariat atau multimodal,
pembentukan skor risiko prediktif, kemudian penerjemahan skor tersebut menjadi
alert melalui ambang tertentu. Pola ini menunjukkan bahwa efektivitas early
warning system tidak hanya ditentukan oleh kemampuan model mengenali pola

16
risiko, tetapi juga oleh cara risiko tersebut dikonversi menjadi sinyal peringatan yang
relevan, tepat waktu, dan dapat ditindaklanjuti [25]–[28].
Pada sektor pertanian, pendekatan berbasis AI mulai digunakan untuk
membangun sistem peringatan dini yang menggabungkan berbagai sumber data
secara simultan. Salah satu penelitian mengembangkan MSPEW-Net, yaitu sistem
peringatan dini berbasis predictive inference yang memanfaatkan data stres
lingkungan, citra UAV atau satelit, serta pola propagasi penyakit tanaman untuk
menghasilkan skor risiko probabilistik [25]. Skor tersebut kemudian digunakan untuk
memicu alert dengan sensitivitas yang disesuaikan terhadap area dan jenis tanaman.
Penelitian lain pada sistem penyimpanan gandum mengembangkan kerangka deep
learning yang menggabungkan klasifikasi kondisi saat ini dengan prediksi distribusi
suhu masa depan untuk mendeteksi risiko kondensasi dan mildew [26]. Temuan ini
menunjukkan bahwa dalam sistem agrifood, AI-based early warning tidak hanya
berfungsi sebagai alat prediksi, tetapi juga sebagai mekanisme identifikasi kondisi
abnormal yang berpotensi menimbulkan kerugian operasional [25], [26].
Selain penerapannya pada pertanian dan penyimpanan pangan, penelitian di
bidang klinis memberikan gambaran yang lebih jelas mengenai bagaimana alert
generation framework dan risk scoring mechanism dievaluasi secara sistematis. Studi
yang membandingkan beberapa early warning scores menunjukkan bahwa sistem
peringatan dapat dibangun dengan dua pendekatan utama, yaitu pendekatan rule-
based dan pendekatan ML-based [27]. Pendekatan rule-based seperti MEWS, NEWS,
dan NEWS2 biasanya menggunakan skor agregat berbasis aturan dan ambang risiko
tertentu, sehingga relatif lebih transparan dan mudah dipahami. Sebaliknya,
pendekatan ML-based seperti eCART, EDI, dan RI memanfaatkan pola data yang
lebih kompleks untuk menghasilkan skor risiko yang lebih adaptif [27].
Perbandingan ini menunjukkan bahwa sistem berbasis AI cenderung memberikan
kemampuan diskriminasi yang lebih baik, tetapi keunggulan tersebut tidak hanya
bergantung pada model, melainkan juga pada desain ambang alert, lead time, serta
beban alarm yang ditimbulkan [27].
Pentingnya evaluasi terhadap false positive juga terlihat jelas pada penelitian
yang memvalidasi sistem VC-MAES untuk memprediksi major adverse events di
bangsal rumah sakit [28]. Dalam penelitian tersebut, model deep learning

17
menghasilkan skor 0–100 yang terus diperbarui secara real-time, lalu dibandingkan
dengan NEWS dan MEWS melalui evaluasi sensitivity, specificity, positive predictive
value, dan false positives per true positive [28]. Hasilnya menunjukkan bahwa sistem
berbasis AI dapat menurunkan false positive burden secara signifikan dibandingkan
pendekatan konvensional. Temuan ini penting karena sistem peringatan dini yang
terlalu sering menghasilkan alarm berlebih dapat menimbulkan alert fatigue,
menurunkan kepercayaan pengguna, serta membebani sumber daya operasional [27],
[28]. Dengan demikian, tantangan utama dalam AI-based early warning system
bukan hanya meningkatkan akurasi prediksi, tetapi juga menjaga agar kualitas alert
tetap seimbang antara sensitivitas, ketepatan, dan utilisasi praktis di lapangan.
Berdasarkan berbagai penelitian tersebut, dapat dilihat bahwa sistem
peringatan dini berbasis AI umumnya dibangun melalui kombinasi model prediktif,
skor risiko, dan mekanisme alert berbasis ambang tertentu [25]–[28]. Pendekatan
ML-based menunjukkan potensi yang lebih tinggi dibandingkan sistem rule-based
yang lebih kaku, tetapi keunggulan tersebut tetap bergantung pada desain mekanisme
alert generation dan pengendalian false positive [25]–[28]. Oleh karena itu,
pengembangan sistem peringatan dini perlu mempertimbangkan tidak hanya
kemampuan model mendeteksi risiko, tetapi juga bagaimana hasil deteksi
diterjemahkan menjadi peringatan yang operasional dan reliabel. Oleh karena itu,
pengembangan sistem peringatan dini pada penelitian ini tidak cukup hanya berfokus
pada kemampuan model mendeteksi risiko, tetapi juga harus mempertimbangkan
bagaimana hasil deteksi diterjemahkan menjadi peringatan yang operasional,
reliabel, dan tidak menimbulkan alarm berlebih. Kondisi ini menegaskan bahwa
sistem deteksi risiko yang baik perlu didukung oleh mekanisme risk scoring dan alert
generation yang terstruktur agar dapat berfungsi sebagai early warning system yang
benar-benar berguna.

18
2.1.7. Ringkasan dan Posisi Penelitian
Berdasarkan kajian terhadap berbagai penelitian terdahulu, dapat
disimpulkan bahwa deteksi anomali, pemodelan risiko, model hybrid, dan sistem
peringatan dini telah berkembang cukup luas pada berbagai bidang, termasuk sistem
industri, keamanan digital, pemantauan operasional, serta sektor pertanian. Dalam
penelitian-penelitian tersebut, pendekatan yang digunakan umumnya terbagi ke
dalam beberapa kelompok utama, yaitu pendekatan berbasis deteksi anomali
unsupervised seperti Isolation Forest, pendekatan probabilistik berbasis Bayesian
Network, termasuk varian classifier yang lebih sederhana seperti Naive Bayes,
pendekatan hybrid yang menggabungkan beberapa model, serta sistem early warning
berbasis skor risiko dan alert generation.
Pendekatan berbasis Isolation Forest menunjukkan keunggulan dalam
mendeteksi anomali pada data multivariat dan berdimensi tinggi tanpa memerlukan
data berlabel. Metode ini efektif untuk mendeteksi observasi yang menyimpang
melalui mekanisme isolasi acak, tetapi kinerjanya sensitif terhadap pengaturan
parameter seperti contamination dan masih memiliki keterbatasan dalam
interpretabilitas probabilistik. Di sisi lain, Bayesian Network unggul dalam
memodelkan ketergantungan antar variabel serta mendukung inferensi risiko melalui
probabilitas posterior. Namun, pendekatan ini sangat dipengaruhi oleh kualitas
struktur directed acyclic graph (DAG) dan menghadapi tantangan komputasional
ketika diterapkan pada data kontinu besar atau struktur yang kompleks.
Sejumlah penelitian juga telah mengembangkan pendekatan hybrid untuk
meningkatkan performa deteksi risiko dan anomali. Model hybrid umumnya
dibangun melalui kombinasi komponen unsupervised, supervised, atau komponen
probabilistik, baik pada level skor, fitur, maupun inferensi. Akan tetapi, sebagian
besar penelitian masih berfokus pada domain tertentu dan belum secara eksplisit
mengintegrasikan Isolation Forest dengan Bayesian Network dalam satu kerangka
deteksi risiko yang terpadu. Pada saat yang sama, penelitian mengenai sistem
peringatan dini berbasis AI menunjukkan bahwa hasil model prediktif umumnya
diterjemahkan ke dalam bentuk skor risiko dan alert berbasis ambang tertentu.
Namun, tantangan seperti false positive, beban alarm, dan reliabilitas alert masih
menjadi persoalan penting dalam penerapan operasional.

19

Dalam sektor pertanian, penelitian terdahulu telah memodelkan berbagai
jenis risiko, seperti risiko harga, risiko cuaca, risiko organisme pengganggu tanaman,
risiko  distribusi,  risiko  tindakan  pengelolaan,  dan  risiko  produksi.  Meskipun
demikian, pemodelan tersebut umumnya masih dilakukan secara terpisah atau hanya
menghubungkan  dua  sampai  tiga  layer  risiko  secara  terbatas.  Belum  banyak
penelitian yang menangani berbagai domain risiko pertanian, seperti harga, cuaca,
OPT, distribusi, tindakan pengelolaan, dan produksi, dalam satu kerangka deteksi
risiko  multi-domain  yang  tetap  mempertahankan  karakteristik  masing-masing
domain dan terhubung dengan mekanisme peringatan dini. Oleh karena itu, masih
terdapat kebutuhan akan pendekatan yang mampu menghubungkan deteksi anomali,
inferensi probabilistik, integrasi multi-domain, dan risk alerting dalam satu kerangka
yang operasional.
Untuk memperjelas posisi penelitian, Tabel 2.1 menyajikan ringkasan lima
penelitian terdahulu yang paling relevan.
 Tabel 2.1 Ringkasan Penelitian Terdahulu
| Peneliti  |         |             | Fitur yang  | Metode    |              |               |
| --------- | ------- | ----------- | ----------- | --------- | ------------ | ------------- |
| No        | Domain  | Pendekatan  |             |           | Hasil Utama  | Keterbatasan  |
| & Tahun   |         |             | Digunakan   | Evaluasi  |              |               |
1  Burney et  Agricultural  Pemodelan  Komponen  R², within  Risiko iklim  Belum
al. (2024)  risks  empiris risiko  cuaca, yield,  R²  menjelaskan  mengintegrasikan
| [3]  |     | iklim  | revenue,      |     | >50% variasi  | OPT dan distribusi  |
| ---- | --- | ------ | ------------- | --- | ------------- | ------------------- |
|      |     |        | loan default  |     | hasil         | dalam satu model    |
pertanian
2  Claudia et  Anomaly  Isolation Forest  Fitur biner  Precision,  IF efektif;  Sensitif terhadap
al. (2025)  detection  +  permission  Recall,  tuning  contamination;
[18]  hyperparameter  request  F1, FPR,  menurunkan  tidak memberi
|     |     | tuning  | Android  | TPR  | false positive  | reasoning      |
| --- | --- | ------- | -------- | ---- | --------------- | -------------- |
|     |     |         |          |      | hingga 50%      | probabilistik  |
3  Stenhouse  Risk  Bayesian  39 faktor  Balanced  BN mampu  Bergantung pada
et al.  modeling  Network +  risiko klinis;  accuracy,  memodelkan  kualitas DAG;
(2025)  simulated  diskretisasi  F1 macro,  dependensi  domain klinis,
 [9], [10]  annealing  KMeans  ROC- variabel  bukan pertanian
|     |     |     |     | AUC  | risiko  |     |
| --- | --- | --- | --- | ---- | ------- | --- |
kompleks

20
Tabel 2.1 (lanjutan)
Peneliti
Fitur yang Metode
No & Domain Pendekatan Hasil Utama Keterbatasan
Digunakan Evaluasi
Tahun
4 Wang et Hybrid Kernel SOM Data Precision, Integrasi Belum
al. anomaly + Bayesian monitoring Recall, unsupervised dan menggunakan IF +
(2025) detection Posterior pompa; F1, lag probabilistik BN; masih spesifik
[15] Inference distribusi time meningkatkan satu domain
probabilitas interpretabilitas
jarak cluster
5 Shyam Early AI-based Sensor Overall Accuracy 94,2%; Tidak
et al. warning EWS; deep lingkungan, accuracy menghasilkan mengintegrasikan
(2025) pertanian learning citra skor risiko seluruh layer risiko
[25] multimodal UAV/satelit, probabilistik dan rantai pasok
pola penyakit alert dini pertanian
Analisis Research Gap dalam penelitian ini adalah sebagai berikut:
a) Sebagian besar penelitian masih menggunakan pendekatan tunggal, baik deteksi
anomali maupun pemodelan probabilistik, sehingga kemampuan untuk
menangkap penyimpangan distribusional dan melakukan penalaran risiko belum
dimanfaatkan secara simultan.
b) Model hybrid yang ada belum banyak mengintegrasikan deteksi anomali berbasis
isolasi dengan inferensi probabilistik berbasis jaringan Bayesian dalam satu
arsitektur yang eksplisit.
c) Penelitian pada sektor pertanian masih cenderung memodelkan risiko secara
parsial, misalnya hanya risiko harga, hanya cuaca, hanya OPT, atau hanya
distribusi.
d) Belum banyak penelitian yang menangani berbagai domain risiko pertanian dalam
satu kerangka deteksi risiko multi-domain dengan tetap mempertahankan
karakteristik masing-masing domain.
e) Sistem peringatan dini berbasis AI umumnya sudah menggunakan skor risiko dan
alert, tetapi belum banyak yang dibangun dari integrasi deteksi anomali dan
probabilistic reasoning untuk mendukung keputusan risiko yang lebih
komprehensif.

21
Posisi penelitian ini adalah sebagai berikut:
a) Mengembangkan model hybrid yang mengintegrasikan Isolation Forest dengan
Bayesian Network dalam satu kerangka analisis risiko, dengan implementasi
komponen Bayesian menggunakan struktur classifier yang bersifat naif berbasis
label dan fitur.
b) Menghubungkan deteksi anomali dengan inferensi probabilistik, sehingga hasil
deteksi tidak berhenti pada identifikasi penyimpangan, tetapi dilanjutkan ke
penalaran risiko.
c) Menangani risiko pada beberapa domain dalam rantai pasok pertanian, yaitu
harga, cuaca, OPT, distribusi, tindakan pengelolaan, dan produksi, melalui
pemodelan per-domain sehingga membentuk sistem deteksi risiko multi-domain
yang lebih terstruktur.
d) Menghasilkan skor risiko hybrid pada setiap domain yang dapat digunakan
sebagai dasar sistem peringatan dini.
e) Memberikan kontribusi metodologis dan aplikatif pada pengembangan sistem
deteksi risiko yang lebih terstruktur, operasional, dan relevan untuk sektor
pertanian.
2.1.8. Kerangka Pemikiran
Rantai pasok pertanian menghadapi risiko dari beberapa domain yang saling
berinteraksi, sehingga pendekatan deteksi satu domain belum mampu
merepresentasikan kondisi risiko secara menyeluruh. Penelitian terdahulu masih
didominasi pendekatan single-domain dan single-model yang memiliki keterbatasan
masing-masing. Isolation Forest sesuai untuk mendeteksi anomali secara
unsupervised, sedangkan Bayesian Network sesuai untuk memodelkan
ketidakpastian probabilistik — keduanya memiliki keterbatasan yang saling
melengkapi. Integrasi keduanya dalam satu kerangka hybrid berpotensi
menghasilkan deteksi risiko multi-domain yang lebih komprehensif. Model hybrid
IF–BN dikembangkan secara per-domain pada enam domain risiko (harga, cuaca,
OPT, distribusi, tindakan pengelolaan, dan produksi) dan dievaluasi pada data multi-
domain rantai pasok pertanian di Kabupaten Sumedang periode 2022–2024 dengan
resolusi mingguan-kecamatan. Penelitian ini memberikan kontribusi metodologis
sebagai dasar pengembangan sistem peringatan dini pada rantai pasok pertanian.

22
Berdasarkan alur pemikiran tersebut, kerangka penelitian ini dapat
digambarkan sebagai berikut.
Gambar 2.1 Kerangka Pemikiran
2.2. Tinjauan Pustaka
2.2.1. Konsep Risiko dan Ketidakpastian
Risiko merupakan konsep yang berkaitan dengan kemungkinan terjadinya
suatu kejadian yang menimbulkan konsekuensi tertentu di bawah kondisi
ketidakpastian [29]. Risiko tidak hanya berhubungan dengan peluang kerugian, tetapi
juga dengan kondisi ketika keputusan harus diambil meskipun hasil akhirnya belum
dapat diketahui secara pasti [29]. Dalam analisis risiko, probabilitas digunakan
sebagai alat kuantitatif untuk merepresentasikan derajat kemungkinan suatu
kejadian, sedangkan ketidakpastian menggambarkan keterbatasan pengetahuan
mengenai apakah, kapan, dan seberapa besar suatu kejadian akan terjadi. Penilaian
risiko dibangun dari kombinasi keduanya, karena keputusan nyata hampir selalu
dilakukan di bawah informasi yang tidak sempurna [29].

23
Pada sistem dinamis, risiko menjadi lebih kompleks karena kondisi sistem
berubah terhadap waktu dan dipengaruhi oleh banyak faktor yang saling berinteraksi
[30]. Ketidakpastian pada sistem seperti ini tidak hanya berasal dari kondisi awal
atau gangguan eksternal, tetapi juga dari bagaimana ketidakpastian tersebut
merambat sepanjang perkembangan sistem [30]. Artinya, perubahan kecil pada
parameter, input, atau lingkungan dapat menghasilkan konsekuensi yang berbeda
seiring berjalannya waktu [30]. Dalam situasi semacam ini, risiko tidak lagi dipahami
sebagai nilai statis, melainkan sebagai sesuatu yang berkembang secara temporal
sesuai dinamika sistem [27].
Dengan demikian, konsep risiko dan ketidakpastian memberikan landasan
penting bagi penelitian ini. Secara umum, risiko dipahami sebagai kemungkinan
munculnya konsekuensi yang merugikan di bawah kondisi ketidakpastian,
sedangkan probabilitas digunakan sebagai sarana untuk merepresentasikan
kemungkinan tersebut. Namun, dalam konteks penelitian ini, risiko dipahami secara
operasional sebagai kondisi penyimpangan signifikan pada indikator domain yang
dapat berfungsi sebagai sinyal awal potensi gangguan pada rantai pasok pertanian.
Pada sistem yang dinamis seperti rantai pasok pertanian, penyimpangan tersebut
dapat berubah mengikuti interaksi antara faktor lingkungan, operasional, dan
ekonomi. Oleh karena itu, pemahaman terhadap risiko, probabilitas, ketidakpastian,
dan anomali menjadi dasar konseptual yang penting sebelum membahas karakteristik
risiko pada rantai pasok pertanian.
2.2.2. Rantai Pasok Pertanian dan Karakteristik Risikonya
Rantai pasok pertanian merupakan sistem yang menghubungkan berbagai
tahapan kegiatan mulai dari produksi di tingkat petani, penanganan pascapanen,
pengolahan, distribusi, hingga produk sampai kepada konsumen akhir [1]. Berbeda
dari rantai pasok pada sektor manufaktur, rantai pasok pertanian memiliki
karakteristik yang lebih sensitif terhadap faktor alam, kualitas produk yang mudah
menurun, serta ketergantungan tinggi pada koordinasi antar pelaku dari hulu hingga
hilir [1]. Struktur ini membuat aliran barang, informasi, dan keputusan dalam sistem
pertanian sangat dipengaruhi oleh kondisi produksi, infrastruktur distribusi, regulasi,
serta perubahan pasar [1].

24
Salah satu karakteristik penting dalam rantai pasok pertanian adalah
volatilitas harga. Harga komoditas pertanian cenderung berfluktuasi akibat
perubahan penawaran dan permintaan, kondisi pasar, kebijakan, serta tekanan
eksternal yang berkaitan dengan faktor agronomis dan iklim [2]. Risiko harga
menjadi penting karena perubahan harga tidak hanya memengaruhi pendapatan
produsen, tetapi juga memengaruhi keputusan pengadaan, penyimpanan, distribusi,
dan konsumsi [2]. Dengan demikian, volatilitas harga dalam sektor pertanian tidak
dapat dipisahkan dari dinamika produksi dan perubahan lingkungan yang
memengaruhi stabilitas pasar [2].
Karakteristik berikutnya adalah ketergantungan terhadap cuaca. Produksi
pertanian sangat dipengaruhi oleh curah hujan, suhu, kekeringan, banjir, gelombang
panas, dan berbagai bentuk anomali iklim lainnya [1], [2]. Ketergantungan ini
menjadikan rantai pasok pertanian lebih rentan terhadap gangguan dibandingkan
banyak sektor lain, karena perubahan cuaca dapat berdampak langsung pada hasil
panen, kualitas produk, ketersediaan pasokan, dan akhirnya harga di pasar [1], [2].
Dengan demikian, cuaca tidak hanya menjadi faktor produksi, tetapi juga menjadi
sumber risiko yang memengaruhi stabilitas keseluruhan rantai pasok pertanian.
Selain itu, rantai pasok pertanian juga memiliki kerentanan distribusi yang
tinggi [1]. Kerentanan ini muncul karena produk pertanian umumnya bersifat mudah
rusak, memerlukan penanganan khusus, bergantung pada infrastruktur transportasi
dan penyimpanan, serta sensitif terhadap keterlambatan dan gangguan logistik [1].
Pada sistem agri-food modern, distribusi yang terganggu dapat menyebabkan
kehilangan kualitas, peningkatan biaya, keterlambatan pasokan, dan bahkan
memperbesar kerugian ekonomi di berbagai titik rantai pasok [1]. Oleh karena itu,
rantai pasok pertanian dapat dipahami sebagai sistem yang secara inheren
menghadapi kombinasi risiko harga, ketergantungan cuaca, dan kerentanan
distribusi, sehingga membutuhkan pendekatan analisis risiko yang lebih terintegrasi
[1], [2].

25
2.2.3. Teori Anomaly Detection
Anomaly detection merupakan proses identifikasi data, pola, atau kejadian
yang menyimpang secara signifikan dari perilaku normal suatu sistem [31]. Dalam
banyak kasus, anomali dipahami sebagai observasi yang tidak mengikuti distribusi
umum data atau menunjukkan karakteristik yang berbeda dibandingkan mayoritas
objek lain. Keberadaan anomali sering dikaitkan dengan kejadian yang jarang
muncul, tidak terduga, atau berpotensi menimbulkan gangguan terhadap sistem yang
diamati. Oleh karena itu, anomaly detection banyak digunakan dalam berbagai
bidang, seperti keamanan siber, pemantauan industri, kesehatan, keuangan, hingga
sistem pertanian, karena mampu membantu mengenali kondisi tidak normal sebelum
berkembang menjadi risiko yang lebih besar [31].
Secara umum, anomali dapat dibedakan menjadi tiga tipe utama, yaitu point
anomaly, contextual anomaly, dan collective anomaly [31]. Point anomaly terjadi
ketika satu observasi tunggal menunjukkan penyimpangan yang jelas dibandingkan
data normal di sekitarnya. Contextual anomaly muncul ketika suatu observasi
dianggap normal dalam satu situasi, tetapi menjadi anomali pada konteks tertentu,
misalnya berdasarkan waktu, lokasi, atau kondisi lingkungan. Sementara itu,
collective anomaly terjadi ketika sekelompok data secara bersama-sama membentuk
pola yang tidak wajar, meskipun tiap titik data secara individual belum tentu terlihat
menyimpang [31]. Pembagian ini menunjukkan bahwa anomali tidak selalu
berbentuk nilai ekstrem tunggal, tetapi dapat juga muncul sebagai pola yang hanya
dapat dikenali melalui hubungan antar data atau melalui konteks kemunculannya.
Berdasarkan ketersediaan label, pendekatan anomaly detection dibedakan
menjadi supervised, semi-supervised, dan unsupervised [31]. Pada sistem nyata, data
anomali cenderung jarang, tidak seimbang, dan sulit dilabeli secara konsisten,
sehingga pendekatan supervised sering tidak praktis [32]. Pendekatan unsupervised
menjadi lebih relevan karena tidak memerlukan label anomali pada tahap pelatihan,
melainkan mendeteksi penyimpangan berdasarkan pola intrinsik data normal [31],
[32]. Pendekatan ini juga lebih fleksibel pada data deret waktu dan multivariat
dengan ketidakpastian tinggi [32]. Dalam penelitian ini, pendekatan unsupervised
menjadi relevan karena risiko pada rantai pasok pertanian dapat muncul dalam
berbagai bentuk penyimpangan yang tidak selalu tersedia labelnya secara lengkap.

26
2.2.4. Teori Isolation Forest
Setelah penerapan Isolation Forest dalam penelitian terdahulu diuraikan pada
Subbab 2.1.2, subbab ini menguraikan landasan teori metode tersebut. Isolation
Forest merupakan metode unsupervised anomaly detection yang dibangun atas
asumsi bahwa anomali umumnya lebih sedikit jumlahnya dan memiliki karakteristik
yang lebih mudah dipisahkan dibandingkan data normal [33].
Konsep utama dalam Isolation Forest adalah path length, yaitu panjang
lintasan dari akar pohon sampai suatu observasi mencapai simpul terminal [34].
Semakin pendek lintasan suatu data, semakin besar kemungkinan data tersebut
merupakan anomali, karena data tersebut dapat dipisahkan dengan lebih sedikit
langkah [34]. Oleh karena itu, keputusan anomali dalam Isolation Forest ditentukan
berdasarkan expected path length, yaitu rata-rata panjang lintasan suatu observasi
pada seluruh pohon dalam hutan isolasi [34]. Nilai ini kemudian dibandingkan
dengan panjang lintasan rata-rata yang diharapkan pada pohon pencarian biner acak,
sehingga diperoleh dasar untuk membedakan antara data normal dan data yang
menyimpang [34].
Agar skor anomali dapat diperbandingkan secara konsisten, Isolation Forest
menggunakan normalisasi terhadap expected path length melalui faktor c(n), yaitu
estimasi panjang lintasan rata-rata pada pohon acak dengan ukuran sampel n [34].
Dengan normalisasi tersebut, skor anomali tidak hanya bergantung pada panjang
lintasan mentah, tetapi juga mempertimbangkan ukuran subsampel yang digunakan
saat membangun pohon [34]. Secara umum, skor yang mendekati 1 menunjukkan
kecenderungan kuat bahwa suatu observasi adalah anomali, sedangkan skor yang
lebih rendah menunjukkan bahwa observasi tersebut lebih dekat pada pola data
normal [34]. Mekanisme ini memberikan dasar statistik yang lebih kuat dalam
interpretasi skor Isolation Forest.
Dari sisi komputasi, Isolation Forest dikenal efisien karena setiap pohon
dibangun menggunakan subsampel acak berukuran terbatas, bukan seluruh data
secara penuh [33]. Karakteristik ini membuat metode tersebut relatif ringan dalam
kebutuhan waktu dan memori dibandingkan pendekatan yang memerlukan
perhitungan pasangan jarak secara menyeluruh atau estimasi distribusi berdimensi
tinggi [33]. Selain itu, pendekatan isolasi acak juga membuat Isolation Forest cukup

27
skalabel untuk data multivariat [33]. Dengan demikian, Isolation Forest dapat
dipahami sebagai metode deteksi anomali yang memanfaatkan random partitioning,
expected path length, normalisasi skor, dan efisiensi komputasi untuk mengenali
penyimpangan data secara efektif, sehingga relevan digunakan sebagai landasan
metode dalam penelitian ini [33], [34].
2.2.5. Teori Bayesian Network
Setelah penerapan Bayesian Network dalam penelitian terdahulu diuraikan
pada Subbab 2.1.3, subbab ini menguraikan landasan teori metode tersebut. Bayesian
Network merupakan model graf probabilistik yang digunakan untuk
merepresentasikan hubungan ketergantungan antar variabel dalam suatu sistem
melalui struktur Directed Acyclic Graph (DAG) [12], [13]. Dalam model ini, setiap
node merepresentasikan variabel acak, sedangkan setiap edge menunjukkan adanya
hubungan ketergantungan probabilistik antar variabel [12], [13]. Dasar teoritis
Bayesian Network berasal dari Teorema Bayes, yaitu prinsip pembaruan probabilitas
suatu kejadian berdasarkan informasi baru yang diamati. Melalui prinsip ini,
Bayesian Network memungkinkan perhitungan probabilitas posterior secara
sistematis ketika terdapat bukti atau observasi baru [13].
Hubungan antar variabel dalam Bayesian Network dinyatakan melalui
conditional probability, yaitu probabilitas suatu variabel dengan syarat nilai variabel
lain telah diketahui [12], [13]. Dengan memanfaatkan conditional probability,
distribusi probabilitas gabungan dari seluruh variabel tidak perlu dihitung secara
penuh, tetapi dapat diuraikan menjadi hasil perkalian probabilitas kondisional
berdasarkan struktur DAG yang digunakan [12]. Mekanisme ini menjadikan
Bayesian Network efisien dalam memodelkan sistem yang kompleks, karena
hubungan antar variabel dapat direpresentasikan secara terstruktur sesuai dependensi
yang dianggap relevan [12], [13].
Struktur DAG memiliki peran yang sangat penting dalam Bayesian Network
karena menentukan arah hubungan antar node serta pola ketergantungan yang
digunakan dalam inferensi [12], [13]. Sifat acyclic berarti grafik tidak boleh
membentuk siklus, sehingga aliran dependensi berjalan secara terarah tanpa kembali
ke node asal [12]. Dengan struktur seperti ini, Bayesian Network tidak hanya
berfungsi sebagai representasi grafis, tetapi juga sebagai kerangka formal untuk

28
menunjukkan bagaimana informasi mengalir dari satu variabel ke variabel lain [12],
[13]. Oleh karena itu, kualitas struktur DAG sangat menentukan kemampuan model
dalam merepresentasikan hubungan probabilistik yang masuk akal dan menghasilkan
inferensi yang akurat [13].
Melalui kombinasi Teorema Bayes, conditional probability, dan struktur
DAG, Bayesian Network mendukung proses probabilistic inference, yaitu penalaran
untuk menghitung probabilitas suatu variabel berdasarkan bukti pada variabel lain
[12], [13]. Inferensi ini dapat bersifat diagnostik, ketika bukti digunakan untuk
menelusuri kemungkinan penyebab, maupun prediktif, ketika kondisi awal
digunakan untuk memperkirakan kejadian berikutnya [12]. Keunggulan tersebut
menjadikan Bayesian Network relevan untuk pemodelan risiko dan pengambilan
keputusan di bawah ketidakpastian, karena model ini mampu menghubungkan
berbagai variabel secara eksplisit dan memperbarui keyakinan secara probabilistik
ketika informasi baru tersedia [12], [13]. Dengan demikian, Bayesian Network
menjadi landasan teoritis yang kuat dalam penelitian ini untuk mendukung analisis
hubungan risiko dan inferensi probabilistik pada sistem yang kompleks.
Dalam penelitian ini, komponen Bayesian Network tidak dibangun sebagai
struktur umum yang kompleks, tetapi dioperasionalkan melalui bentuk classifier
dengan struktur naif, di mana label berperan sebagai parent bagi fitur-fitur observasi.
Oleh karena itu, pembahasan pada subbab berikutnya difokuskan pada Naive
Bayesian Network sebagai bentuk implementatif yang relevan dengan kebutuhan
klasifikasi probabilistik dalam penelitian ini.
2.2.6. Naive Bayesian Network (Label Features)
Naive Bayesian Network merupakan bentuk paling sederhana dari Bayesian
Network Classifier, di mana variabel kelas atau label ditempatkan sebagai parent
bagi seluruh fitur yang digunakan dalam proses klasifikasi [35], [36]. Dalam struktur
ini, setiap fitur diasumsikan bergantung langsung pada label, sehingga arah hubungan
probabilistik dibangun dari label menuju fitur. Bentuk tersebut membuat model
menjadi sederhana, efisien, dan mudah digunakan untuk klasifikasi karena distribusi
probabilitas gabungan dapat diuraikan ke dalam probabilitas prior kelas dan
probabilitas kondisional masing-masing fitur terhadap kelas [35], [36].

29
Karakteristik utama Naive Bayesian Network adalah asumsi conditional
independence, yaitu setiap fitur dianggap saling bebas bersyarat setelah nilai label
diketahui [35], [36]. Dengan kata lain, jika kelas suatu observasi telah ditentukan,
maka nilai satu fitur dianggap tidak lagi bergantung pada fitur lain. Asumsi ini
memang cukup kuat dan sering kali tidak sepenuhnya terpenuhi pada data nyata,
tetapi justru menjadi dasar yang membuat Naive Bayes tetap sederhana dan efisien
secara komputasi [36]. Dalam pengembangannya, model seperti Tree-Augmented
Naive Bayes dan struktur berbasis k-tree dikembangkan untuk melonggarkan asumsi
independensi penuh tersebut dengan menambahkan dependensi terbatas antar fitur,
meskipun label tetap dipertahankan sebagai node utama dalam struktur klasifikasi
[35], [36].
Dalam proses pembelajaran, parameter pada Naive Bayesian Network
diestimasi melalui probabilitas prior kelas dan probabilitas kondisional fitur terhadap
kelas [35], [36]. Pada pendekatan Bayesian, estimasi parameter dapat diperkuat
dengan penggunaan prior agar probabilitas yang diperoleh lebih stabil, terutama
ketika data terbatas atau terdapat kombinasi fitur-kelas yang jarang muncul Salah
satu prior yang dikenal dalam pembelajaran jaringan Bayesian adalah Bayesian
Dirichlet equivalent uniform (BDeu prior), yang dalam kondisi tertentu dapat
digunakan untuk memberikan regularisasi pada estimasi parameter, terutama saat
data terbatas atau terdapat kombinasi fitur–kelas yang jarang muncul. Namun, secara
umum inti pembelajaran pada Naive Bayesian Network tetap terletak pada estimasi
prior kelas dan probabilitas kondisional fitur terhadap kelas [35], [36].
Dengan demikian, Naive Bayesian Network dapat dipahami sebagai model
probabilistik yang menempatkan label sebagai parent bagi seluruh fitur,
menggunakan asumsi conditional independence untuk menyederhanakan
perhitungan, dan mengestimasi parameter melalui probabilitas prior serta
probabilitas kondisional yang dapat diperkuat dengan prior Bayesian [35], [36].
Struktur ini menjadikan Naive Bayesian Network efisien untuk klasifikasi
probabilistik, sekaligus menjadi dasar bagi pengembangan struktur yang lebih
kompleks dalam keluarga Bayesian Network Classifiers. Dalam penelitian ini,
komponen Bayesian Network dioperasionalkan dalam bentuk Naive Bayesian

30
Network dengan estimasi parameter berbasis Bayesian estimator dan BDeu prior,
yang akan diuraikan secara teknis pada Bab 3.
2.2.7. Model Hybrid Dalam Sistem Cerdas
Setelah strategi integrasi hybrid dalam penelitian terdahulu diuraikan pada
Subbab 2.1.4, subbab ini menguraikan landasan teori model hybrid. Model hybrid
merupakan pendekatan yang menggabungkan dua atau lebih metode untuk
memanfaatkan keunggulan masing-masing komponen [14], [16]. Berbeda dari
ensemble yang umumnya menggabungkan beberapa model untuk menghasilkan
keputusan akhir yang lebih stabil, model hybrid menekankan integrasi
antarkomponen yang dapat terjadi pada level fitur, skor, keputusan, maupun alur
inferensi [14]. Dengan demikian, model hybrid tidak sekadar mengumpulkan banyak
model, tetapi membangun mekanisme kerja yang saling melengkapi antara metode
yang berbeda karakteristiknya.
Strategi integrasi pada model hybrid secara umum dapat dibedakan menjadi
score-level fusion dan feature-level fusion. Pada score-level fusion, skor keluaran dari
beberapa model dinormalisasi terlebih dahulu agar berada pada skala yang
sebanding, kemudian digabungkan melalui rata-rata, penjumlahan berbobot, atau
mekanisme ambang tertentu [14]. Pendekatan ini relatif sederhana karena setiap
model tetap bekerja secara mandiri dan integrasi dilakukan pada tahap akhir.
Sebaliknya, feature-level fusion dilakukan dengan menggunakan keluaran suatu
model sebagai fitur tambahan bagi model lain sebelum keputusan akhir dihasilkan
[16]. Strategi ini memungkinkan sistem menangkap hubungan yang lebih kaya
antarkomponen, meskipun lebih kompleks dibandingkan score-level fusion [16].
Dalam penelitian ini, feature-level fusion dipilih sebagai strategi integrasi karena
sesuai dengan karakteristik Isolation Forest sebagai penghasil skor anomali dan
Bayesian Network sebagai mesin inferensi probabilistik berbasis fitur.

31
2.2.8. Integrasi Skor dan Strategi Agregasi
Dalam sistem deteksi anomali yang melibatkan lebih dari satu model,
keluaran dari tiap komponen perlu diintegrasikan agar menghasilkan keputusan akhir
yang konsisten [14], [16]. Integrasi dilakukan melalui strategi agregasi skor, yaitu
proses menggabungkan nilai keluaran dari beberapa model ke dalam satu skor akhir
yang mewakili tingkat risiko atau keabnormalan suatu observasi [14]. Pendekatan ini
penting karena setiap model dapat menghasilkan skala skor yang berbeda, sehingga
tanpa mekanisme agregasi yang tepat, hasil keputusan akhir dapat menjadi tidak
stabil atau sulit dibandingkan secara langsung [14], [16].
Beberapa strategi agregasi yang umum digunakan adalah mean aggregation
yang memberikan bobot setara pada setiap model, weighted aggregation yang
memberikan bobot berbeda sesuai tingkat kepentingan model, serta score
normalization yang menyamakan skala skor antarmodel [14], [16]. Setelah skor akhir
diperoleh, tahap berikutnya adalah thresholding, yaitu penentuan ambang keputusan
untuk membedakan kondisi normal dan kondisi berisiko, baik secara tetap maupun
adaptif [14], [16]. Dalam penelitian ini, konsep normalisasi skor dan thresholding
menjadi landasan penting untuk mekanisme integrasi hasil deteksi, sedangkan
strategi score-level aggregation tidak digunakan secara langsung karena penelitian
ini memilih feature-level fusion, yaitu menggunakan skor Isolation Forest sebagai
fitur tambahan bagi Bayesian Network, bukan menggabungkan skor antarmodel pada
tahap akhir.
2.2.9. Evaluasi Model Klasifikasi dan Deteksi Anomali
Evaluasi model deteksi anomali dilakukan untuk menilai sejauh mana model
mampu membedakan antara data normal dan data anomali secara tepat [32], [37].
Dalam praktiknya, hasil prediksi model umumnya dirangkum terlebih dahulu dalam
confusion matrix, yaitu tabel yang memuat jumlah true positive, true negative, false
positive, dan false negative [32]. Berdasarkan komponen tersebut, berbagai metrik
evaluasi dihitung untuk menggambarkan performa model dari sudut pandang yang
berbeda. Penggunaan lebih dari satu metrik menjadi penting karena kinerja model
deteksi anomali tidak dapat diwakili secara memadai hanya oleh satu ukuran,
terutama pada data yang cenderung tidak seimbang [32], [37].

32
Metrik dasar yang paling umum digunakan adalah precision dan recall [32],
[37]. Precision menunjukkan proporsi data yang diprediksi sebagai anomali dan
benar-benar merupakan anomali, sehingga metrik ini berkaitan dengan ketepatan
alarm yang dihasilkan model [32]. Sementara itu, recall menunjukkan proporsi
anomali aktual yang berhasil dideteksi oleh model, sehingga metrik ini
menggambarkan sensitivitas model terhadap kejadian menyimpang [32]. Dalam
sistem deteksi anomali, kedua metrik tersebut memiliki peran yang sama penting,
karena model yang terlalu sensitif dapat menghasilkan banyak false positive,
sedangkan model yang terlalu konservatif dapat gagal mengenali anomali yang
seharusnya terdeteksi [32].
Untuk menyeimbangkan kedua aspek tersebut, sering digunakan F1-score,
yaitu rata-rata harmonik dari precision dan recall yang memberikan gambaran
performa lebih seimbang ketika ketepatan dan kelengkapan deteksi sama-sama
penting [32]. Selain itu, evaluasi sering menggunakan ROC-AUC, yang mengukur
kemampuan model membedakan kelas positif dan negatif pada berbagai ambang
keputusan [32], [37]. Pada data tidak seimbang, ROC-AUC tetap berguna untuk
memberikan gambaran diskriminasi model secara umum, sedangkan kombinasi
precision, recall, dan F1-score memberikan pandangan yang lebih spesifik terhadap
kinerja deteksi pada kelas minoritas [37].
Dalam deteksi anomali, evaluasi model tidak hanya menilai performa
statistik, tetapi juga relevansinya untuk penerapan nyata [32]. Metrik confusion
matrix, precision, recall, F1-score, dan ROC-AUC memberikan sudut pandang yang
berbeda terhadap kualitas deteksi, dan kombinasi kelimanya dapat menghasilkan
penilaian yang utuh [32], [37]. Dalam penelitian ini, kelima metrik tersebut
digunakan sebagai dasar evaluasi performa ketiga model (Isolation Forest, Bayesian
Network, dan model hybrid), dengan recall diberikan prioritas khusus karena
penelitian ini diposisikan sebagai dasar bagi sistem peringatan dini yang
menempatkan keandalan deteksi anomali sebagai pertimbangan utama.

33
2.2.10. Penanganan Data Imbalance
Masalah imbalanced classification muncul ketika distribusi kelas dalam data
tidak seimbang, sehingga jumlah observasi pada satu kelas jauh lebih besar
dibandingkan kelas lainnya [38]. Kondisi ini umum dijumpai pada banyak kasus
nyata, termasuk deteksi anomali, karena kejadian yang dianggap penting justru sering
muncul sebagai kelas minoritas [38]. Akibat ketidakseimbangan tersebut, model
klasifikasi cenderung lebih mudah mempelajari pola kelas mayoritas dan
mengabaikan karakteristik kelas minoritas. Dampaknya, model dapat terlihat
memiliki performa tinggi secara umum, tetapi sebenarnya gagal mengenali kejadian
minoritas yang justru menjadi fokus utama analisis [38].
Salah satu pendekatan yang banyak digunakan untuk mengatasi masalah
tersebut adalah cost-sensitive learning, yaitu pendekatan yang memberikan bobot
atau biaya kesalahan yang berbeda pada tiap kelas [39]. Dalam kerangka ini,
kesalahan dalam memprediksi kelas minoritas biasanya diberi biaya lebih besar
dibandingkan kesalahan pada kelas mayoritas, sehingga model terdorong untuk lebih
memperhatikan observasi yang jarang muncul [39]. Pendekatan ini penting karena
pada banyak aplikasi, termasuk deteksi risiko dan anomali, false negative sering lebih
merugikan daripada false positive, sehingga proses pembelajaran perlu
mempertimbangkan ketidaksimetrian biaya kesalahan tersebut [39].
Selain melalui pembobotan biaya, penanganan data imbalance juga dapat
dilakukan melalui threshold adjustment, yaitu penyesuaian ambang keputusan
klasifikasi agar lebih sesuai dengan distribusi kelas dan tujuan evaluasi [39]. Dalam
kondisi tidak seimbang, penggunaan ambang standar sering kali menghasilkan
keputusan yang terlalu berpihak pada kelas mayoritas. Oleh karena itu, ambang
keputusan dapat digeser untuk meningkatkan sensitivitas terhadap kelas minoritas,
meskipun hal ini biasanya disertai trade-off terhadap jumlah false positive [39].
Penyesuaian ambang ini menjadi relevan karena hasil probabilitas atau skor keluaran
model tidak selalu optimal jika langsung diterjemahkan dengan aturan keputusan
yang kaku.
Dengan demikian, penanganan data imbalance tidak hanya berkaitan dengan
distribusi kelas yang tidak merata, tetapi juga dengan bagaimana model dilatih dan
bagaimana keputusan akhir ditetapkan [38], [39]. Cost-sensitive learning membantu

34
model belajar dengan mempertimbangkan perbedaan biaya kesalahan, sedangkan
threshold adjustment membantu menyeimbangkan sensitivitas dan spesifisitas sesuai
tujuan penggunaan model [39]. Dalam penelitian ini, pemahaman terhadap masalah
imbalance menjadi penting karena deteksi risiko dan anomali umumnya berhadapan
dengan kejadian minoritas, sehingga strategi pembelajaran dan penentuan ambang
perlu dirancang secara lebih hati-hati agar model tidak bias terhadap pola mayoritas.

BAB III
METODOLOGI
3.1. Jenis Penelitian
Penelitian ini merupakan penelitian kuantitatif berbasis data dengan desain
eksperimental komputasional. Pendekatan kuantitatif digunakan karena penelitian ini
mengolah data numerik dari beberapa domain risiko secara sistematis untuk
menghasilkan skor risiko dan keputusan deteksi, sedangkan desain eksperimental
komputasional ditunjukkan melalui perancangan model, pelatihan, pengujian, dan
evaluasi kinerja secara terstruktur menggunakan data historis.
Penelitian ini diposisikan sebagai model development and evaluation, yaitu
penelitian yang menempatkan model machine learning sebagai objek utama yang
dikembangkan dan dianalisis kinerjanya. Dengan posisi ini, penelitian tidak diarahkan
pada rekayasa sistem informasi atau pembangunan aplikasi operasional, melainkan pada
pembangunan dan pengujian model untuk mendeteksi risiko multi-domain pada rantai
pasok pertanian.
Pendekatan yang digunakan bersifat data-driven modeling, yaitu pemodelan yang
dibangun berdasarkan pola yang dipelajari dari data historis multi-domain pada rantai
pasok pertanian, bukan dari aturan pakar yang ditetapkan secara tetap. Data yang
digunakan merupakan data sekunder periode 2022–2024 pada wilayah Kabupaten
Sumedang, sehingga proses pemodelan dilakukan tanpa pengumpulan data primer
melalui survei, wawancara, atau observasi lapangan.
Desain penelitian disusun dalam bentuk comparative analysis terhadap tiga model
deteksi risiko, yaitu Isolation Forest, Bayesian Network, dan model hybrid Isolation
Forest–Bayesian Network. Perbandingan dilakukan untuk mengukur kinerja setiap model
dalam menghasilkan skor risiko dan keputusan deteksi, sehingga dapat dianalisis sejauh
mana integrasi kedua pendekatan memberikan peningkatan dibandingkan penggunaan
model tunggal.
35

36
3.2. Metode Pengembangan Model
Metode pengembangan model dalam penelitian ini disusun sebagai pipeline yang
terdiri atas enam fase, mulai dari pengumpulan data hingga evaluasi kinerja. Pipeline ini
dirancang agar setiap fase menghasilkan keluaran yang dapat digunakan sebagai masukan
pada fase berikutnya, sehingga proses pengembangan model berjalan secara berurutan
dan dapat ditelusuri pada setiap tahapnya. Alur pipeline secara umum ditunjukkan pada
Gambar 3.1.
Gambar 3.1 Pipeline Pengembangan Model
a) Data Acquisition. Fase ini mencakup pengumpulan data sekunder dari instansi
yang berwenang untuk seluruh domain risiko yang dianalisis, yaitu harga, cuaca,
organisme pengganggu tanaman (OPT), distribusi, tindakan pengelolaan, dan
produksi. Data yang digunakan merupakan data historis pada wilayah Kabupaten
Sumedang periode 2022–2024.
b) Data Preprocessing. Fase ini mencakup integrasi data dari berbagai domain ke
dalam struktur yang konsisten, pembersihan data, penyesuaian format atribut
waktu, penanganan nilai yang tidak sesuai, serta penyelarasan resolusi temporal
antar domain ke unit analisis penelitian. Tujuan utama fase ini adalah memastikan
data dari setiap domain berada dalam kondisi yang layak dan seragam untuk
diproses pada fase berikutnya.
c) Feature Engineering. Fase ini mencakup pembentukan fitur turunan dari data
hasil preprocessing serta pembentukan label risiko yang digunakan sebagai target
dalam proses pemodelan. Fitur turunan dibentuk untuk merepresentasikan pola
risiko pada masing-masing domain, sedangkan label risiko dibentuk melalui
pendekatan statistik untuk domain non-cuaca dan pendekatan berbasis aturan
untuk domain cuaca.

37
d) Model Development. Fase ini mencakup pengembangan dua model dasar secara
per-domain, yaitu model Isolation Forest dan model Bayesian Network. Isolation
Forest dikembangkan untuk menghasilkan skor anomali berdasarkan pola
penyimpangan data, sedangkan Bayesian Network dikembangkan untuk
menghasilkan probabilitas risiko berdasarkan hubungan antara label dan fitur
observasi.
e) Model Integration (Hybrid). Fase ini mencakup pengembangan model hybrid
Isolation Forest–Bayesian Network melalui feature-level fusion, yaitu integrasi
pada tingkat fitur dengan menggunakan skor anomali Isolation Forest sebagai
salah satu masukan bagi Bayesian Network. Model hybrid menghasilkan
probabilitas risiko yang memuat informasi penyimpangan distribusional sekaligus
penalaran probabilistik.
f) Evaluation. Fase ini mencakup penentuan threshold keputusan deteksi serta
evaluasi kinerja ketiga model, yaitu Isolation Forest, Bayesian Network, dan
model hybrid Isolation Forest–Bayesian Network. Evaluasi dilakukan dengan
membandingkan keluaran model terhadap label risiko yang telah dibentuk pada
fase sebelumnya, baik secara keseluruhan maupun secara per-domain.
3.3. Objek Penelitian
Objek dalam penelitian ini adalah deteksi risiko multi-domain pada rantai pasok
pertanian yang direpresentasikan melalui data historis pada enam domain risiko, yaitu
harga, cuaca, organisme pengganggu tanaman (OPT), distribusi, tindakan pengelolaan,
dan produksi. Penelitian berfokus pada pengembangan model untuk mendeteksi
penyimpangan signifikan pada indikator-indikator yang berkaitan dengan keenam
domain tersebut. Risiko dalam penelitian ini tidak dipahami sebagai kerugian aktual yang
telah terjadi, melainkan sebagai kondisi penyimpangan pada indikator domain yang dapat
berfungsi sebagai sinyal awal potensi gangguan dalam rantai pasok pertanian.
Penelitian ini menggunakan data dengan cakupan wilayah Kabupaten Sumedang
dan periode waktu 2022–2024. Setiap domain memiliki karakteristik data, entitas, dan
indikator yang berbeda, sehingga keenam domain tersebut diposisikan sebagai sub-system
dalam sistem rantai pasok pertanian yang lebih besar. Pemodelan tidak dilakukan dalam
satu struktur tunggal yang menggabungkan seluruh domain, melainkan secara per-domain

38
agar karakteristik data masing-masing tetap terjaga. Meskipun pemodelan dilakukan
secara terpisah, antar domain tetap memiliki relasi konseptual yang saling memengaruhi.
3.3.1. Domain Risiko Penelitian
Domain risiko dalam penelitian ini diposisikan sebagai sub-system yang
masing-masing memiliki definisi operasional, variabel pengamatan, dan peran yang
berbeda dalam rantai pasok pertanian. Antar sub-system tersebut terdapat relasi
konseptual yang saling memengaruhi, sehingga gangguan pada satu domain
berpotensi merambat ke domain lain. Penjelasan masing-masing domain diuraikan
sebagai berikut.
a) Domain Harga
Domain harga merupakan sub-system yang merepresentasikan dinamika harga
komoditas pertanian pada pasar tertentu di wilayah Kabupaten Sumedang. Secara
operasional, risiko pada domain ini didefinisikan sebagai kondisi penyimpangan
signifikan pada nilai harga komoditas dibandingkan pola harga normalnya.
Penyimpangan tersebut dapat berupa lonjakan harga maupun penurunan harga
yang tidak wajar pada periode tertentu.
Variabel utama pada domain ini adalah nilai harga komoditas pada satuan
rupiah per kilogram, dengan entitas pengamatan berupa kombinasi tanggal, pasar,
komoditas, dan saluran harga. Variabel-variabel ini memungkinkan dinamika
harga dianalisis pada level yang lebih spesifik dibandingkan harga pasar secara
umum.
Dalam rantai pasok pertanian, domain harga memiliki relasi konseptual dengan
domain produksi dan domain distribusi. Penurunan produksi pada wilayah tertentu
berpotensi memengaruhi harga di pasar terkait, sedangkan gangguan distribusi
antar pasar dapat menyebabkan perbedaan harga yang signifikan. Sebaliknya,
perubahan harga juga dapat memengaruhi pola arus distribusi komoditas antar
pasar.

39
b) Domain Cuaca
Domain cuaca merupakan sub-system yang merepresentasikan kondisi
meteorologis yang berpotensi mempengaruhi aktivitas budidaya dan rantai pasok
pertanian di wilayah Kabupaten Sumedang. Secara operasional, risiko pada
domain ini didefinisikan sebagai kondisi cuaca ekstrem yang menyimpang dari
pola musimannya, seperti curah hujan sangat tinggi, suhu ekstrem, maupun
periode kering yang panjang.
Variabel utama pada domain ini meliputi suhu minimum, suhu maksimum,
suhu rata-rata, kelembapan rata-rata, curah hujan, lama penyinaran matahari, serta
variabel kecepatan dan arah angin. Berbeda dengan domain lain yang memiliki
entitas pada level kecamatan, domain cuaca diposisikan sebagai data pada tingkat
wilayah Kabupaten Sumedang secara keseluruhan. Hal ini disebabkan data cuaca
yang digunakan berasal dari satu sumber observasi resmi yang mencakup wilayah
Sumedang, sehingga belum tersedia variasi pengukuran pada level kecamatan.
Konsekuensinya, kondisi cuaca pada minggu yang sama berlaku sebagai common
factor bagi seluruh kecamatan dalam wilayah Sumedang.
Dalam rantai pasok pertanian, domain cuaca memiliki relasi konseptual yang
luas dengan domain lain. Anomali cuaca seperti curah hujan tinggi atau suhu
ekstrem berpotensi memicu peningkatan kejadian OPT, sedangkan kondisi cuaca
yang tidak mendukung dapat berdampak langsung pada hasil produksi pertanian.
Karakteristik ini menempatkan domain cuaca sebagai salah satu sub-system yang
memengaruhi banyak domain lain pada rantai pasok pertanian.
c) Domain Organisme Pengganggu Tanaman (OPT)
Domain OPT merupakan sub-system yang merepresentasikan kondisi
gangguan biologis pada komoditas pertanian di wilayah Kabupaten Sumedang.
Secara operasional, risiko pada domain ini didefinisikan sebagai kondisi
peningkatan kejadian OPT yang menyimpang dari pola normalnya, termasuk
kondisi ketika nilai kejadian melampaui ambang ekonomi yang telah ditetapkan
untuk komoditas dan jenis OPT tertentu.
Variabel utama pada domain ini meliputi nilai kejadian OPT, ambang ekonomi
sebagai nilai acuan pemantauan, serta status melampaui ambang sebagai indikator
yang menunjukkan tingkat keparahan kejadian. Entitas pengamatan berupa

40
kombinasi tanggal, kecamatan, komoditas, dan jenis OPT, sehingga pola kejadian
OPT dapat dianalisis pada level yang spesifik untuk setiap kombinasi tersebut.
Dalam rantai pasok pertanian, domain OPT memiliki relasi konseptual yang
erat dengan beberapa domain lain. Domain ini menerima pengaruh dari domain
cuaca, karena anomali curah hujan, suhu, dan kelembapan dapat memicu
peningkatan kejadian OPT. Selain itu, domain OPT memiliki relasi dua arah
dengan domain tindakan pengelolaan, yaitu lonjakan kejadian OPT memicu
peningkatan tindakan pengendalian, sedangkan tindakan pengelolaan yang efektif
berkontribusi pada penurunan kejadian OPT pada periode berikutnya. Pada
akhirnya, domain OPT juga memengaruhi domain produksi, karena serangan OPT
yang tidak terkendali berpotensi menurunkan hasil panen
d) Domain Distribusi
Domain distribusi merupakan sub-system yang merepresentasikan aliran
komoditas pertanian antar pasar di wilayah Kabupaten Sumedang. Secara
operasional, risiko pada domain ini didefinisikan sebagai kondisi penyimpangan
signifikan pada pola arus barang antar pasar, terutama berupa penurunan volume
aliran yang dapat mengindikasikan adanya gangguan dalam proses distribusi.
Variabel utama pada domain ini meliputi volume aliran komoditas, harga pada
pasar asal, harga pada pasar tujuan, biaya distribusi, dan waktu tempuh distribusi.
Entitas pengamatan berupa kombinasi tanggal aliran, pasar asal, pasar tujuan,
komoditas, dan saluran distribusi. Dengan struktur entitas tersebut, pola aliran
komoditas dapat dianalisis pada level yang lebih spesifik untuk setiap pasangan
pasar dan komoditas.
Dalam rantai pasok pertanian, domain distribusi memiliki relasi dua arah
dengan domain harga. Perubahan harga pada pasar asal maupun pasar tujuan dapat
memengaruhi pola arus distribusi komoditas, sedangkan gangguan pada distribusi
berpotensi menyebabkan ketimpangan harga antar pasar. Karakteristik ini
menempatkan domain distribusi sebagai sub-system yang menjadi penghubung
antar pasar pada rantai pasok pertanian, sekaligus sebagai titik yang rentan
terhadap akumulasi risiko dari domain lain.

41
e) Domain Tindakan Pengelolaan
Domain tindakan pengelolaan merupakan sub-system yang merepresentasikan
respons atau intervensi terhadap kejadian OPT pada komoditas pertanian di
wilayah Kabupaten Sumedang. Secara operasional, risiko pada domain ini
didefinisikan sebagai kondisi penyimpangan signifikan pada pola tindakan
pengelolaan, baik berupa peningkatan intensitas tindakan yang tidak biasa maupun
pola respons yang tidak sesuai dengan kondisi normal pengelolaan.
Variabel utama pada domain ini meliputi luas area yang ditangani, dosis atau
intensitas tindakan, biaya total pengelolaan, jam kerja yang digunakan, metode
pengelolaan yang diterapkan, serta nilai kejadian OPT setelah tindak lanjut
sebagai indikator hasil tindakan. Entitas pengamatan berupa kombinasi tanggal
tindakan, kecamatan, komoditas, jenis OPT, dan metode pengelolaan, sehingga
pola intervensi dapat dianalisis pada level yang spesifik untuk setiap kombinasi
tersebut.
Dalam rantai pasok pertanian, domain tindakan pengelolaan memiliki relasi
dua arah dengan domain OPT. Lonjakan kejadian OPT memicu peningkatan
tindakan pengendalian, sedangkan tindakan yang efektif berkontribusi pada
penurunan kejadian OPT pada periode berikutnya. Selain itu, domain tindakan
pengelolaan juga memiliki relasi konseptual dengan domain produksi secara tidak
langsung, karena tindakan pengendalian yang berhasil membantu
mempertahankan hasil panen melalui pengendalian kejadian OPT. Karakteristik
ini menempatkan domain tindakan pengelolaan sebagai sub-system yang berperan
sebagai mekanisme respons sekaligus pelindung hasil produksi pada rantai pasok
pertanian.
f) Domain Produksi
Domain produksi merupakan sub-system yang merepresentasikan hasil
aktivitas budidaya pertanian di wilayah Kabupaten Sumedang. Secara operasional,
risiko pada domain ini didefinisikan sebagai kondisi penyimpangan signifikan
pada indikator produksi pertanian, terutama berupa penurunan luas panen, total
produksi, atau produktivitas yang tidak wajar dibandingkan pola produksi
normalnya.

42
Variabel utama pada domain ini meliputi luas panen dalam satuan hektar, total
produksi dalam satuan ton, dan produktivitas dalam satuan ton per hektar. Entitas
pengamatan berupa kombinasi bulan, kecamatan, dan komoditas. Karena resolusi
data produksi bersifat bulanan, domain ini memiliki karakteristik temporal yang
berbeda dengan domain lain yang umumnya tersedia pada resolusi yang lebih
halus. Konsekuensi dari karakteristik ini adalah perlunya penyelarasan resolusi
temporal pada tahap preprocessing agar data produksi dapat dianalisis bersama
domain lain pada unit analisis yang seragam.
Dalam rantai pasok pertanian, domain produksi memiliki posisi sebagai sub-
system yang menerima dampak dari beberapa domain sebelumnya sekaligus
memengaruhi domain berikutnya. Domain produksi menerima pengaruh dari
domain cuaca, karena kondisi meteorologis ekstrem dapat menurunkan hasil
panen, dan dari domain OPT, karena serangan OPT yang tidak terkendali
berdampak langsung pada produksi. Domain produksi juga menerima pengaruh
tidak langsung dari domain tindakan pengelolaan melalui mekanisme
pengendalian OPT. Pada akhirnya, domain produksi memengaruhi domain harga,
karena penurunan hasil produksi pada wilayah tertentu dapat memicu kenaikan
harga pada pasar terkait. Posisi ini menempatkan domain produksi sebagai sub-
system yang menjadi titik akumulasi dampak risiko dari domain biofisik, sekaligus
titik awal pengaruh terhadap domain ekonomi pada rantai pasok pertanian.

43

3.3.2.  Entitas, Variabel, Satuan, dan Sumber Data
Subbab ini menjelaskan entitas pengamatan, variabel, satuan pengukuran,
dan sumber data yang digunakan pada masing-masing domain penelitian. Penjelasan
ini bertujuan untuk memperjelas struktur data yang menjadi dasar dalam proses
analisis dan pemodelan. Ringkasan teknis mengenai entitas, variabel, satuan, dan
sumber data disajikan pada Tabel 3.1.
Tabel 3.1 Variabel, Satuan, dan Sumber Data per Domain
| Domain  | Variabel     | Satuan  | Sumber Data                |
| ------- | ------------ | ------- | -------------------------- |
|         | price_value  | Rp/kg   | Dinas Pertanian Kabupaten  |
Sumedang
Harga  price_channel_code  Kategorikal  Dinas Pertanian Kabupaten
|     |     | (WHOLESALE_TRAD,  | Sumedang  |
| --- | --- | ----------------- | --------- |
RETAIL_TRAD,
RETAIL_MODERN)
|     | TN      | °C (suhu minimum)    | BMKG  |
| --- | ------- | -------------------- | ----- |
|     | TX      | °C (suhu maksimum)   | BMKG  |
|     | TAVG    | °C (suhu rata-rata)  | BMKG  |
|     | RH_AVG  | % (kelembapan rata-  | BMKG  |
rata)
|     | RR  | mm (curah hujan)  | BMKG  |
| --- | --- | ----------------- | ----- |
Cuaca
|     | SS  | jam (lama penyinaran  | BMKG  |
| --- | --- | --------------------- | ----- |
matahari)
|     | FF_X  | m/s (kecepatan angin  | BMKG  |
| --- | ----- | --------------------- | ----- |
maksimum)
|     | FF_AVG  | m/s (kecepatan angin  | BMKG  |
| --- | ------- | --------------------- | ----- |
rata-rata)
|     | DDD_X  | derajat (arah angin saat  | BMKG  |
| --- | ------ | ------------------------- | ----- |
kecepatan maksimum)
|     | DDD_CAR  | Kategorikal (arah angin  | BMKG  |
| --- | -------- | ------------------------ | ----- |
terbanyak)

44

Tabel 3.1 (lanjutan)
| Domain  | Variabel  | Satuan  | Sumber Data  |
| ------- | --------- | ------- | ------------ |
incidence_value  bervariasi per jenis  Dinas Pertanian Kabupaten
|     |     | OPT (ekor/rumpun, %  | Sumedang  |
| --- | --- | -------------------- | --------- |
insidensi, %
keparahan)
|     | ae_value  | bervariasi per jenis  | Dinas Pertanian Kabupaten  |
| --- | --------- | --------------------- | -------------------------- |
OPT
|     |     | OPT (sesuai satuan  | Sumedang  |
| --- | --- | ------------------- | --------- |
kejadian)
|     | over_ae  | Boolean (status   | Dinas Pertanian Kabupaten  |
| --- | -------- | ----------------- | -------------------------- |
|     |          | melampaui ambang  | Sumedang                   |
ekonomi)
|     | flow_volume  | ton  | Dinas Pertanian Kabupaten  |
| --- | ------------ | ---- | -------------------------- |
Sumedang
|     | price_origin    | Rp/kg (harga pasar  | Dinas Pertanian Kabupaten  |
| --- | --------------- | ------------------- | -------------------------- |
|     |                 | asal)               | Sumedang                   |
|     | price_dest      | Rp/kg (harga pasar  | Dinas Pertanian Kabupaten  |
|     |                 | tujuan)             | Sumedang                   |
|     | transport_cost  | Rp per transaksi    | Dinas Pertanian Kabupaten  |
Sumedang
|             | handling_cost  | Rp per transaksi  | Dinas Pertanian Kabupaten  |
| ----------- | -------------- | ----------------- | -------------------------- |
| Distribusi  |                |                   | Sumedang                   |
|             | other_cost     | Rp per transaksi  | Dinas Pertanian Kabupaten  |
Sumedang
lead_time_days  hari (waktu tempuh  Dinas Pertanian Kabupaten
|     |     | distribusi)  | Sumedang  |
| --- | --- | ------------ | --------- |
channel_name  Kategorikal (Eceran,  Dinas Pertanian Kabupaten
|     |     | Grosir)  | Sumedang  |
| --- | --- | -------- | --------- |
intermediary_type  Kategorikal (Agen,  Dinas Pertanian Kabupaten
|     |     | Koperasi, Pedagang  | Sumedang  |
| --- | --- | ------------------- | --------- |
Pengumpul)
incidence_value  bervariasi per metode  Dinas Pertanian Kabupaten
|     |     | pemantauan  | Sumedang  |
| --- | --- | ----------- | --------- |
incidence_value_followup  bervariasi per metode  Dinas Pertanian Kabupaten
|     |     | pemantauan  | Sumedang  |
| --- | --- | ----------- | --------- |
Tindakan
Pengelolaan  ae_value  bervariasi per jenis  Dinas Pertanian Kabupaten
|     |          | OPT               | Sumedang                   |
| --- | -------- | ----------------- | -------------------------- |
|     | over_ae  | Boolean (status   | Dinas Pertanian Kabupaten  |
|     |          | melampaui ambang  | Sumedang                   |
ekonomi)

45

Tabel 3.1 (lanjutan)
| Domain  | Variabel      | Satuan            | Sumber Data                |
| ------- | ------------- | ----------------- | -------------------------- |
|         | trigger_type  | Kategorikal (AE)  | Dinas Pertanian Kabupaten  |
Sumedang
management_method_name  Kategorikal (Kimia)  Dinas Pertanian Kabupaten
Sumedang
|     | area_treated  | hektar  | Dinas Pertanian Kabupaten  |
| --- | ------------- | ------- | -------------------------- |
Sumedang
Tindakan
Pengelolaan
dose_or_intensity  bervariasi sesuai  Dinas Pertanian Kabupaten
|     |             | metode pengelolaan  | Sumedang                   |
| --- | ----------- | ------------------- | -------------------------- |
|     | cost_total  | Rp per kejadian     | Dinas Pertanian Kabupaten  |
Sumedang
|     | labor_hours  | jam  | Dinas Pertanian Kabupaten  |
| --- | ------------ | ---- | -------------------------- |
Sumedang
harvest_area_ha  hektar (luas panen)  Dinas Pertanian Kabupaten
Sumedang
production_ton  ton (total produksi)  Dinas Pertanian Kabupaten
Produksi
Sumedang
|     | yield_ton_per_ha  | ton/hektar       | Dinas Pertanian Kabupaten  |
| --- | ----------------- | ---------------- | -------------------------- |
|     |                   | (produktivitas)  | Sumedang                   |

46
3.3.3. Unit Analisis Penelitian
Unit analisis dalam penelitian ini adalah observasi mingguan pada level
kecamatan untuk setiap domain risiko. Dengan demikian, satu pengamatan dalam
pemodelan merepresentasikan kondisi suatu domain risiko pada satu kecamatan
dalam satu minggu tertentu. Penetapan unit analisis pada level kecamatan dan
resolusi mingguan diarahkan untuk menjamin konsistensi pemodelan, sehingga
kinerja deteksi dapat diperbandingkan secara setara antar domain dan antar wilayah.
3.4. Teknik Pengumpulan Data
Penelitian ini menggunakan data sekunder berupa arsip historis yang diperoleh
secara resmi dari instansi yang berwenang, bukan data primer yang dikumpulkan
langsung melalui survei, wawancara, atau observasi lapangan. Pendekatan ini dipilih
karena data operasional pada masing-masing domain risiko telah tersedia dalam bentuk
catatan historis di instansi terkait, sehingga proses pengumpulan data dilakukan melalui
akuisisi arsip dan studi dokumen.
Data pada domain cuaca diperoleh dari Badan Meteorologi, Klimatologi, dan
Geofisika (BMKG) Stasiun Klimatologi Bandung yang mencakup wilayah Kabupaten
Sumedang. Sementara itu, data pada domain harga, organisme pengganggu tanaman
(OPT), distribusi, tindakan pengelolaan, dan produksi diperoleh dari Dinas Pertanian
Kabupaten Sumedang dengan pendampingan langsung dari dosen pembimbing. Seluruh
data yang digunakan mencakup periode 2022–2024 dan diterima dalam bentuk arsip
digital sebagai masukan pada tahapan pemrosesan data penelitian.
Validasi data dilakukan melalui tiga lapisan pemeriksaan untuk memastikan data
yang diterima layak digunakan sebagai bahan pemodelan:
a) Validasi sumber, yaitu memastikan bahwa data berasal dari instansi resmi
yang memiliki otoritas dan rekam jejak pencatatan yang terstandarisasi pada
bidangnya.
b) Validasi struktural, yaitu pemeriksaan kelengkapan kolom, konsistensi format
atribut waktu, ketersediaan nilai pada periode 2022–2024, dan keberadaan
kolom identitas entitas yang dibutuhkan untuk pemodelan.
c) Validasi nilai, yaitu pemeriksaan terhadap keberadaan nilai yang tidak masuk
akal pada pengukuran masing-masing domain.

47
3.5. Teknik Analisis Data
Teknik analisis data dalam penelitian ini dilakukan melalui serangkaian tahapan
yang dirancang untuk membangun dan mengevaluasi model deteksi risiko multi-domain
pada rantai pasok pertanian. Tahapan tersebut meliputi pembentukan label risiko, pra-
pemrosesan data dan feature engineering, pengembangan model Isolation Forest,
pengembangan model Bayesian Network, pengembangan model hybrid Isolation Forest–
Bayesian Network, penentuan threshold, serta evaluasi model. Seluruh tahapan analisis
disusun secara berurutan agar keluaran dari setiap tahap dapat digunakan sebagai
masukan pada tahap berikutnya.
3.5.1. Pembentukan Label Risiko
Pembentukan label risiko dilakukan untuk menghasilkan target yang
digunakan dalam pelatihan dan evaluasi model. Label utama yang digunakan dalam
penelitian ini adalah label biner label_is_anomaly yang menunjukkan apakah suatu
observasi tergolong anomali atau tidak, sedangkan label kategori label_severity
digunakan untuk menunjukkan tingkat keparahan anomali pada tiga kategori, yaitu
Normal, Waspada, dan Bahaya. Pelatihan dan evaluasi model berfokus pada label
biner, sementara label kategori digunakan sebagai informasi pendukung untuk
keperluan interpretasi hasil.
a) Pembentukan Label Pada Domain Non – Cuaca
Untuk domain non-cuaca, yaitu harga, OPT, distribusi, tindakan pengelolaan,
dan produksi, label anomali dibentuk menggunakan pendekatan deviasi robust
berbasis Median Absolute Deviation (MAD). Pendekatan ini dipilih karena lebih
tahan terhadap nilai ekstrem dibandingkan pendekatan berbasis simpangan baku,
sehingga lebih sesuai untuk data operasional pertanian yang sering mengandung
nilai ekstrem alami. Nilai deviasi robust untuk setiap observasi dihitung
menggunakan rumus berikut:
|x − median(x)|
AE =
dev MAD
dengan :
MAD = median(|x − median(x)|)

48
Pada kondisi ketika nilai MAD bernilai nol, simpangan baku digunakan sebagai
pengganti, dan apabila simpangan baku juga bernilai nol, penyebut ditetapkan
pada nilai konstan yang sangat kecil agar perhitungan tetap dapat dilakukan.
Setelah nilai deviasi diperoleh, ditentukan ambang anomali per kelompok
menggunakan kuantil 0,975 dari distribusi AEdev dalam kelompok tersebut.
Kelompok dibentuk berdasarkan kombinasi kolom identitas yang tersedia, seperti
risk_name, market_id, commodity_id, dan district_id. Apabila jumlah data dalam
suatu kelompok kurang dari 200 baris, digunakan ambang global yang dihitung
dari seluruh data domain. Suatu observasi diberi label anomali (label_is_anomaly
= 1) apabila nilai deviasinya melebihi ambang yang berlaku pada kelompoknya,
dan label normal (label_is_anomaly = 0) apabila tidak.
b) Pembentukan Label Pada Domain Cuaca
Berbeda dengan domain non-cuaca, domain cuaca menggunakan pendekatan
berbasis aturan (rule-based). Pendekatan ini dipilih karena variabel cuaca
memiliki pola musiman yang kuat, sehingga penyimpangan yang relevan secara
agronomis lebih sesuai didefinisikan melalui aturan yang merepresentasikan
kondisi cuaca ekstrem. Tiga aturan utama digunakan dalam penelitian ini, yaitu
ExtremeRain, HeatStress, dan DrySpell, dengan ketentuan sebagai berikut:
(1) ExtremeRain aktif apabila curah hujan harian (RR) lebih besar atau sama
dengan 50 mm per hari, atau melebihi median musiman ditambah dua kali
nilai interquartile range (IQR) musiman.
(2) HeatStress aktif apabila suhu rata-rata harian (TAVG) lebih besar atau
sama dengan 32 °C, atau melebihi median musiman ditambah dua kali
IQR musiman.
(3) DrySpell aktif apabila curah hujan bernilai nol selama sedikitnya tujuh
hari berturut-turut.
Suatu observasi cuaca diberi label label_is_anomaly = 1 apabila salah satu atau
lebih aturan tersebut aktif.

49
c) Pembentukan Label Pada Domain Cuaca
Setelah label biner terbentuk, observasi yang tergolong anomali
(label_is_anomaly = 1) diberi kategori tingkat keparahan menggunakan label
label_severity dengan tiga kategori:
(1) Normal, untuk observasi dengan label_is_anomaly = 0.
(2) Waspada, untuk observasi anomali dengan tingkat penyimpangan
moderat.
(3) Bahaya, untuk observasi anomali dengan tingkat penyimpangan tinggi.
Pada domain non-cuaca, batas antara kategori Waspada dan Bahaya ditentukan
berdasarkan persentil AEdev pada kelompok yang sama. Pada domain cuaca,
kategori Bahaya diberikan apabila dua atau lebih aturan aktif secara bersamaan,
sedangkan kategori Waspada diberikan apabila hanya satu aturan yang aktif.
3.5.2. Preprocessing dan Feature Engineering
Tahap preprocessing dan feature engineering dilakukan untuk memastikan
bahwa data dari setiap domain berada dalam kondisi yang layak dan seragam
sebelum digunakan pada tahap pemodelan, serta untuk membentuk fitur turunan
yang dapat menangkap pola risiko pada masing-masing domain. Tahap ini mencakup
pembersihan data, handling missing value, normalisasi, temporal alignment yang
meliputi agregasi resolusi halus dan bridging resolusi kasar ke unit analisis
mingguan, penyelarasan entitas spasial, serta feature engineering.
a) Handling Missing Value
Sebelum penanganan missing value dilakukan, terlebih dahulu dilakukan
standardisasi nilai missing dengan mengganti penanda non-standar yang umum
digunakan dalam pencatatan instansi seperti tanda hubung "—", angka 8888, dan
9999 menjadi nilai NaN, sehingga dapat ditangani secara konsisten pada tahap
berikutnya. Penanganan missing value selanjutnya dilakukan dengan strategi yang
disesuaikan terhadap karakteristik masing-masing model. Pada model Isolation
Forest, missing value diisi menggunakan median per kelompok identitas sebelum
data dimasukkan ke dalam model. Pendekatan median dipilih karena lebih tahan
terhadap nilai ekstrem dibandingkan rata-rata, dan konsisten dengan pendekatan
robust yang diterapkan sepanjang penelitian ini. Pada model Bayesian Network,
missing value ditangani secara implisit pada tahap diskretisasi, sehingga setiap

50
fitur numerik diubah menjadi kategori diskret tanpa mengharuskan imputasi nilai
eksplisit. Untuk baris data yang tidak memiliki identitas entitas wajib seperti
district_id, dilakukan penghapusan baris karena entitas tersebut diperlukan untuk
pemodelan pada level kecamatan.
b) Normalisasi
Normalisasi dilakukan untuk menyeragamkan skala fitur numerik sebelum
digunakan sebagai masukan model. Penelitian ini menggunakan RobustScaler,
yaitu metode normalisasi berbasis median dan interquartile range (IQR), bukan
rata-rata dan simpangan baku seperti pada StandardScaler. RobustScaler dipilih
karena lebih tahan terhadap pengaruh nilai ekstrem, sehingga sesuai untuk data
deteksi anomali yang justru mengandung observasi ekstrem sebagai target deteksi.
Selain normalisasi fitur masukan, skor anomali dari Isolation Forest juga
dinormalisasi ke rentang 0 hingga 1 untuk memudahkan integrasi dengan
komponen Bayesian Network pada tahap feature-level fusion. Fitur kategorikal
tidak dimasukkan sebagai input langsung pada model Isolation Forest, dan untuk
model Bayesian Network, fitur numerik diubah menjadi bentuk diskret melalui
pendekatan quantile-based binning yang akan dijelaskan pada Subbab 3.5.4
c) Temporal Alignment
Temporal alignment dilakukan untuk menyelaraskan data dari berbagai domain
ke unit analisis mingguan sebagaimana ditetapkan pada Subbab 3.3.3. Karena data
asli memiliki resolusi yang berbeda-beda antar domain, temporal alignment
mencakup dua arah penyelarasan: agregasi dari resolusi lebih halus ke mingguan,
dan bridging dari resolusi lebih kasar ke mingguan. Strategi penyelarasan per
domain dirangkum pada Tabel 3.2.

51
Tabel 3.2 Strategi Temporal Alignment per Domain
Domain Resolusi Asli Strategi Detail
Harga Harian Agregasi → mingguan Rata-rata price_value
per minggu
Cuaca Harian Agregasi → mingguan Curah hujan (RR)
dijumlah; variabel suhu,
kelembapan,
penyinaran, dan angin
dirata-ratakan per
minggu
OPT Mingguan - Pemastian indeks
minggu (week_start)
konsisten
Distribusi Per transaksi Agregasi → mingguan Total flow_volume,
jumlah transaksi, rata-
rata harga dan biaya per
minggu
Tindakan Pengelolaan Per kejadian Agregasi → mingguan Jumlah kejadian, total
area_treated, total
cost_total, total
labor_hours per minggu
Produksi Bulanan Bridging → mingguan Nilai bulanan di-
broadcast ke seluruh
minggu dalam bulan
tersebut
d) Feature Engineering
Setelah data diselaraskan ke unit analisis mingguan, dilakukan feature
engineering untuk membentuk fitur turunan yang dapat menangkap pola risiko
pada masing-masing domain. Fitur dikelompokkan ke dalam beberapa kategori,
yaitu fitur dasar yang berasal langsung dari variabel domain, fitur lag untuk
menangkap temporal jangka pendek dan menengah, fitur rolling untuk menangkap
tren dan variabilitas dalam jendela waktu bergerak, fitur tanggal untuk musim,
serta fitur lintas-domain berupa variabel cuaca yang dimasukkan ke domain OPT,
tindakan pengelolaan, dan produksi sesuai relasi konseptual yang telah dijelaskan
pada Subbab 3.3.1. Fitur kategorikal seperti saluran harga, metode pemantauan,
dan saluran distribusi diubah ke representasi numerik melalui label encoding agar
dapat digunakan sebagai masukan model.

52
Untuk menghindari kebocoran informasi (data leakage) antara fitur dan label,
skor Anomaly Evidence yang digunakan pada pembentukan label di Subbab 3.5.1
tidak digunakan sebagai fitur masukan model. Fitur masukan dibentuk dari
variabel mentah dan turunan temporalnya, sehingga model belajar mengenali pola
anomali dari data observasi, bukan dari sinyal yang sudah dipakai untuk
membentuk label. Pemisahan ini penting untuk menjaga validitas evaluasi model.
3.5.3. Pengembangan Model Isolation Forest
Pengembangan model Isolation Forest dilakukan untuk menghasilkan
komponen deteksi anomali berbasis unsupervised learning pada setiap domain risiko.
Isolation Forest dipilih karena mampu mengenali penyimpangan pada data
multivariat melalui mekanisme isolasi acak tanpa memerlukan label pada tahap
pelatihan, serta relatif efisien untuk diterapkan pada domain risiko dengan
karakteristik distribusi yang berbeda-beda [33], [34]. Pemodelan dilakukan secara
per-domain, sehingga setiap domain memiliki model Isolation Forest tersendiri yang
dilatih pada data hasil feature engineering sebagaimana dijelaskan pada Subbab
3.5.2.
a) Parameter Model
Konfigurasi parameter model Isolation Forest yang digunakan pada penelitian
ini meliputi n_estimators, contamination, max_samples, dan random_state.
Parameter n_estimators menentukan jumlah pohon isolasi yang dibangun dalam
ensemble, sedangkan contamination menentukan proporsi anomali yang
diasumsikan terdapat dalam data dan berpengaruh langsung pada ambang
keputusan model. Parameter max_samples menentukan ukuran subsampel yang
digunakan untuk membangun setiap pohon, dan random_state digunakan untuk
menjaga konsistensi hasil pelatihan pada setiap eksekusi.
Berdasarkan praktik umum pemodelan Isolation Forest dan pertimbangan
karakteristik data penelitian, kandidat awal parameter yang akan digunakan
sebagai titik mula tuning adalah n_estimators = 300, contamination = 0,02,
max_samples = “auto”, dan random_state = 42. Pemilihan n_estimators lebih
besar dari nilai default 100 ditujukan untuk meningkatkan kestabilan skor anomali,
sedangkan contamination = 0,02 ditetapkan dengan asumsi proporsi anomali yang
relatif rendah pada data operasional pertanian. Nilai max_samples = “auto”

53
membuat ukuran subsampel mengikuti ketentuan minimum antara 256 dan jumlah
observasi tersedia, sehingga model tetap efisien meskipun ukuran data berbeda
antar domain.
b) Strategi Tuning Parameter
Karena performa Isolation Forest sensitif terhadap konfigurasi parameter,
terutama contamination [17], [18] penelitian ini menerapkan strategi tuning untuk
memperoleh konfigurasi yang sesuai dengan karakteristik data setiap domain.
Tuning dilakukan dengan pendekatan eksplorasi terbatas pada parameter utama,
yaitu n_estimators dan contamination, dengan mempertimbangkan kestabilan
skor anomali dan kecocokan terhadap label operasional yang telah dibentuk pada
Subbab 3.5.1.
Untuk parameter n_estimators, dieksplorasi beberapa nilai dalam rentang yang
umum digunakan untuk memastikan stabilitas skor tidak terlalu sensitif terhadap
jumlah pohon. Untuk parameter contamination, dilakukan penyesuaian secara
adaptif berdasarkan proporsi label positif pada data latih per domain, sehingga
nilai contamination setiap domain dapat berbeda mengikuti karakteristik distribusi
anomali masing-masing. Hasil tuning dievaluasi menggunakan metrik kinerja
yang dijelaskan pada Subbab 3.5.7, dengan pembagian data berbasis waktu untuk
menghindari kebocoran informasi dari data uji ke proses pelatihan.
c) Output Model
Keluaran utama model Isolation Forest berupa skor anomali yang
merepresentasikan tingkat penyimpangan suatu observasi terhadap pola data
normal. Skor mentah yang dihasilkan oleh fungsi scoring model terlebih dahulu
dinegasikan agar nilai yang lebih tinggi merepresentasikan tingkat anomali yang
lebih tinggi, kemudian dinormalisasi ke rentang 0 hingga 1 menggunakan
MinMaxScaler. Normalisasi ini dilakukan agar skor lebih mudah diperbandingkan
antar observasi dalam domain yang sama, serta dapat digunakan sebagai masukan
pada tahap feature-level fusion yang dijelaskan pada Subbab 3.5.5.
Pada tahap ini, Isolation Forest berperan sebagai komponen yang menangkap
sinyal penyimpangan distribusional pada setiap domain risiko. Skor yang
dihasilkan tidak langsung diterjemahkan menjadi keputusan deteksi, melainkan
diteruskan ke mekanisme threshold yang dijelaskan pada Subbab 3.5.6, atau
diintegrasikan dengan komponen Bayesian Network pada model hybrid.

54
3.5.4. Pengembangan Model Bayesian Network
Pengembangan model Bayesian Network dilakukan untuk menghasilkan
komponen inferensi probabilistik pada setiap domain risiko. Bayesian Network
dipilih karena mampu merepresentasikan hubungan antara variabel observasi dan
label risiko melalui struktur graf probabilistik, serta dapat menghasilkan probabilitas
anomali yang lebih informatif dibandingkan keluaran biner [9], [12], [13].
Pemodelan dilakukan secara per-domain agar karakteristik masing-masing domain
tetap terjaga, sehingga setiap domain memiliki model Bayesian Network tersendiri
yang dilatih pada data hasil feature engineering sebagaimana dijelaskan pada Subbab
3.5.2.
a) Struktur DAG dan Pendekatan Naive Bayes
Struktur graf yang digunakan dalam penelitian ini adalah Directed Acyclic
Graph (DAG) dengan pendekatan Naive Bayes, yaitu struktur sederhana di mana
label risiko ditempatkan sebagai parent node terhadap seluruh fitur observasi.
Struktur DAG yang digunakan dapat dinyatakan sebagai berikut :
label → feature ,feature ,…,feature
is 1 2 N
anomaly
dengan label label_is_anomaly sebagai parent node tunggal yang memiliki
panah ke seluruh fitur observasi (baik fitur dasar, lag, rolling, tanggal, lintas-
domain, maupun kategorikal). Struktur ini bersifat tetap dan tidak dipelajari secara
otomatis melalui structure learning, sehingga konsistensi bentuk model dapat
dijaga di seluruh domain.
Pemilihan pendekatan Naive Bayes dilakukan dengan beberapa pertimbangan.
Pertama, pendekatan ini memiliki efisiensi komputasi yang tinggi karena setiap
fitur diasumsikan saling bebas bersyarat terhadap label, sehingga estimasi
parameter dan inferensi dapat dilakukan dengan cepat meskipun jumlah fitur per
domain mencapai sepuluh hingga dua belas variabel. Kedua, pendekatan ini
menghindari kebutuhan structure learning yang membutuhkan biaya komputasi
tinggi dan tidak selalu menghasilkan struktur yang dapat ditafsirkan. Ketiga,
struktur Naive Bayes telah terbukti efektif untuk klasifikasi probabilistik pada
berbagai pemodelan risiko [11], dan cocok untuk kebutuhan penelitian ini yang
berfokus pada kemampuan model menghasilkan probabilitas anomali, bukan pada
penalaran kausal antar fitur.

55
b) Conditional Probability Table (CPT)
Setiap simpul pada Bayesian Network memiliki Conditional Probability Table
(CPT) yang menyimpan probabilitas nilai simpul tersebut dengan syarat nilai
simpul parent-nya. Pada struktur Naive Bayes yang digunakan, CPT terbagi
menjadi dua jenis. Pertama, CPT untuk simpul label berupa probabilitas prior dari
masing-masing kelas label (normal dan anomali) yang diestimasi dari distribusi
label pada data latih. Kedua, CPT untuk setiap simpul fitur berupa probabilitas
kondisional fitur terhadap label, yaitu peluang fitur mengambil nilai diskret
tertentu pada kondisi label normal maupun label anomali.
Estimasi parameter CPT dilakukan menggunakan Bayesian estimator dengan
prior Bayesian Dirichlet equivalent uniform (BDeu). Penggunaan prior ini
bertujuan menjaga kestabilan estimasi probabilitas, terutama pada kombinasi nilai
fitur dan label yang jarang muncul di data latih. Tanpa prior, kombinasi yang tidak
pernah teramati akan menghasilkan probabilitas nol yang dapat menyebabkan
inferensi tidak stabil. Dengan prior BDeu, probabilitas pada kombinasi tersebut
tetap terdefinisi dengan nilai kecil yang masuk akal, sehingga model tetap dapat
melakukan inferensi pada data uji yang mengandung kombinasi baru.
c) Output Model
Keluaran utama model Bayesian Network berupa probabilitas posterior
anomali, yaitu peluang suatu observasi tergolong anomali dengan syarat nilai fitur-
fiturnya. Probabilitas ini diperoleh melalui inferensi probabilistik pada struktur
DAG menggunakan aturan Bayes, di mana CPT yang telah diestimasi dari data
latih digunakan untuk menghitung peluang label kondisional terhadap kombinasi
nilai fitur observasi. Berbeda dengan Isolation Forest yang menghasilkan skor
anomali berbasis penyimpangan distribusional, Bayesian Network menghasilkan
ukuran probabilitas yang dapat diinterpretasikan sebagai derajat keyakinan model
terhadap status anomali suatu observasi. Probabilitas ini selanjutnya digunakan
baik sebagai keluaran model tunggal pada tahap evaluasi, maupun sebagai
komponen pada model hybrid Isolation Forest–Bayesian Network yang dijelaskan
pada Subbab 3.5.5.

56
3.5.5. Pengembangan Model Hybrid Isolation Forest–Bayesian Network
Pengembangan model hybrid Isolation Forest–Bayesian Network dilakukan
untuk mengintegrasikan dua pendekatan deteksi yang memiliki karakteristik
berbeda, yaitu Isolation Forest sebagai komponen deteksi anomali berbasis isolasi
distribusional, dan Bayesian Network sebagai komponen inferensi probabilistik.
Integrasi ini ditujukan untuk memanfaatkan kekuatan masing-masing komponen,
sehingga model dapat menghasilkan probabilitas risiko yang memuat informasi
penyimpangan distribusional sekaligus penalaran probabilistik. Pemodelan
dilakukan secara per-domain, sehingga setiap domain memiliki model hybrid
tersendiri yang dilatih pada data hasil feature engineering sebagaimana dijelaskan
pada Subbab 3.5.2.
a) Strategi Feature-Level Fusion
Penelitian ini menggunakan strategi feature-level fusion, yaitu integrasi pada
tingkat fitur dengan menjadikan keluaran dari Isolation Forest sebagai salah satu
masukan bagi Bayesian Network. Strategi ini berbeda dengan score-level fusion
yang menggabungkan keluaran kedua model secara langsung pada tahap akhir,
misalnya melalui rata-rata atau penjumlahan skor.
Pemilihan feature-level fusion didasarkan pada beberapa pertimbangan.
Pertama, strategi ini memungkinkan Bayesian Network memodelkan hubungan
probabilistik antara skor Isolation Forest dan label risiko bersama dengan fitur
observasi lainnya, sehingga skor anomali tidak diperlakukan sebagai informasi
terpisah, melainkan terintegrasi dalam kerangka inferensi probabilistik. Kedua,
strategi ini menghasilkan satu keluaran tunggal berupa probabilitas posterior dari
Bayesian Network, sehingga tidak menimbulkan ambiguitas yang dapat muncul
ketika dua keluaran model paralel memberikan sinyal yang bertentangan. Ketiga,
strategi ini lebih sesuai dengan kebutuhan penelitian yang menjadikan probabilitas
risiko sebagai keluaran operasional model deteksi, bukan sekadar skor agregat.

57
b) Alur Pengembangan Model Hybrid
Alur pengembangan model hybrid dilakukan secara sekuensial, dimulai dari
pelatihan Isolation Forest, dilanjutkan dengan diskretisasi skor anomali, dan
diakhiri dengan pelatihan Bayesian Network yang memuat skor anomali sebagai
salah satu fitur. Alur tersebut diilustrasikan pada Gambar 3.2.
Gambar 3.2 Alur Pengembangan Model Hybrid
Berdasarkan Gambar 3.2, alur pengembangan model hybrid dapat dijabarkan
dalam empat tahap. Pertama, Isolation Forest dilatih pada fitur asli domain untuk
menghasilkan skor anomali ternormalisasi if_score_norm pada rentang 0 hingga
1, sebagaimana dijelaskan pada Subbab 3.5.3. Kedua, skor anomali tersebut
didiskretkan menjadi if_score_disc melalui quantile-based binning dengan empat
bin (Q1, Q2, Q3, dan Q4), konsisten dengan strategi diskretisasi yang diterapkan
pada fitur numerik lain. Ketiga, Bayesian Network dilatih dengan masukan berupa
fitur asli domain ditambah if_score_disc sebagai fitur tambahan, mengikuti
struktur Naive Bayes yang sama seperti yang dijelaskan pada Subbab 3.5.4.
Keempat, model hybrid menghasilkan probabilitas posterior risiko sebagai
keluaran akhir.

58
Struktur graf pada model hybrid tetap mengikuti pendekatan Naive Bayes
dengan label label_is_anomaly sebagai parent node, namun dengan tambahan
if_score_disc sebagai salah satu fitur anak. Struktur DAG model hybrid dapat
dinyatakan sebagai berikut:
label → feature ,feature ,…,feature ,if_score_disc
is 1 2 N
anomaly
Dengan struktur ini, perbedaan antara model Bayesian Network tunggal dan
model hybrid hanya terletak pada keberadaan if_score_disc sebagai fitur
tambahan, sehingga perbedaan kinerja pada tahap evaluasi dapat sepenuhnya
dikaitkan dengan kontribusi skor Isolation Forest. Estimasi parameter Conditional
Probability Table (CPT) untuk if_score_disc dilakukan dengan pendekatan yang
sama seperti fitur lain, yaitu menggunakan Bayesian estimator dengan prior
Bayesian Dirichlet equivalent uniform (BDeu)
c) Output Model Hybrid
Keluaran utama model hybrid berupa probabilitas posterior anomali yang dihasilkan
oleh Bayesian Network setelah memuat if_score_disc sebagai salah satu fitur masukan.
Probabilitas ini dapat diinterpretasikan sebagai derajat keyakinan model terhadap status
anomali suatu observasi, dengan tambahan informasi penyimpangan distribusional yang
ditangkap oleh Isolation Forest.
Berbeda dengan model Isolation Forest tunggal yang menghasilkan skor berbasis
isolasi, dan model Bayesian Network tunggal yang hanya memuat fitur observasi domain,
model hybrid menghasilkan probabilitas yang memuat dua jenis informasi sekaligus,
yaitu informasi penyimpangan distribusional dari Isolation Forest dan informasi
kondisional probabilistik dari Bayesian Network. Probabilitas ini menjadi keluaran utama
yang akan digunakan pada mekanisme threshold keputusan deteksi yang dijelaskan pada
Subbab 3.5.6, dan diperbandingkan dengan keluaran model tunggal pada tahap evaluasi
yang dijelaskan pada Subbab 3.5.7.

59
3.5.6. Mekanisme Threshold dan Keputusan Deteksi
Mekanisme threshold dan keputusan deteksi dilakukan untuk mengubah
keluaran model yang berbentuk skor kontinu menjadi keputusan biner anomali atau
normal, sekaligus menentukan tingkat keparahan anomali sebagaimana didefinisikan
pada Subbab 3.5.1. Mekanisme ini berlaku pada ketiga model yang dikembangkan,
yaitu Isolation Forest, Bayesian Network, dan model hybrid Isolation Forest–
Bayesian Network, sehingga keluaran ketiga model dapat diperbandingkan dalam
kondisi keputusan deteksi yang setara.
a) Penentuan Threshold Static
Penelitian ini menggunakan pendekatan static threshold, yaitu nilai ambang
yang ditentukan sekali pada tahap pelatihan dan digunakan secara tetap pada tahap
pengujian. Threshold dihitung secara per-domain, yaitu setiap domain risiko
memiliki nilai threshold tersendiri yang dihitung dari distribusi skor data latih
pada domain tersebut. Pendekatan per-domain dipilih karena distribusi skor
anomali pada setiap domain memiliki karakteristik yang berbeda, sehingga
threshold tunggal yang berlaku seragam untuk seluruh domain dapat
menyebabkan model menjadi terlalu sensitif untuk domain tertentu dan terlalu
konservatif untuk domain lain.
Nilai threshold setiap domain ditetapkan menggunakan kuantil 0,98 dari
distribusi skor data latih, yang berarti 2% observasi dengan skor tertinggi
diidentifikasi sebagai kandidat anomali. Pemilihan kuantil 0,98 didasarkan pada
konsistensi dengan asumsi proporsi anomali rendah pada data operasional
pertanian, sebagaimana juga digunakan pada parameter contamination = 0,02
model Isolation Forest yang dijelaskan pada Subbab 3.5.3. Untuk setiap model
dan setiap domain, threshold dihitung secara terpisah, sehingga total terdapat
threshold yang berbeda-beda untuk kombinasi (model, domain) pada penelitian
ini.

60
b) Pertimbangan Static dan Dynamic Threshold
Selain static threshold, dalam praktik deteksi anomali dikenal pula pendekatan
dynamic threshold, yaitu threshold yang berubah-ubah mengikuti konteks waktu,
jendela bergerak, atau perubahan distribusi data. Kedua pendekatan memiliki
karakteristik yang berbeda. Static threshold menawarkan keunggulan berupa
konsistensi keputusan antar observasi, kemudahan reproduksi hasil, dan
kemudahan implementasi pada sistem yang akan digunakan secara operasional.
Sementara itu, dynamic threshold menawarkan adaptabilitas terhadap perubahan
distribusi data, sehingga dapat lebih responsif terhadap pola musiman atau
pergeseran tren.
Pada penelitian ini, static threshold dipilih sebagai pendekatan utama karena
beberapa pertimbangan. Pertama, model yang dikembangkan ditujukan sebagai
komponen sistem peringatan dini yang membutuhkan keputusan yang konsisten
dan dapat ditelusuri kembali. Threshold yang berubah-ubah dapat menyulitkan
operator dalam memahami alasan munculnya alert tertentu. Kedua, distribusi data
latih pada periode 2022–2024 relatif stabil, sehingga tidak terdapat urgensi yang
kuat untuk menggunakan threshold yang adaptif terhadap waktu. Ketiga, static
threshold lebih mudah dipertahankan secara metodologis karena nilai ambangnya
tetap dan tidak bergantung pada parameter eksternal yang dapat menimbulkan
ambiguitas. Pendekatan dynamic threshold dapat dipertimbangkan sebagai arah
penelitian lanjutan apabila distribusi data pada periode mendatang menunjukkan
pergeseran yang signifikan.
c) Cost-Sensitive Threshold
Untuk memperkuat pendekatan static threshold, penelitian ini menerapkan
cost-sensitive adjustment yang mempertimbangkan asimetri biaya kesalahan
deteksi. Pada konteks deteksi risiko rantai pasok pertanian, biaya melewatkan
anomali nyata (false negative) umumnya lebih besar dibandingkan biaya alarm
palsu (false positive). Anomali yang tidak terdeteksi berpotensi menyebabkan
kerugian operasional yang signifikan, sedangkan alarm palsu hanya menambah
beban verifikasi yang relatif terbatas. Oleh karena itu, threshold dirancang agar
lebih agresif dalam menangkap anomali, dengan trade-off berupa peningkatan
jumlah false positive yang dapat diterima.

61
Penyesuaian cost-sensitive dilakukan dengan asumsi rasio biaya false negative
terhadap false positive sebesar 5 banding 1. Rasio ini dipilih sebagai asumsi awal
yang masuk akal untuk konteks penelitian ini, mengikuti praktik umum pada
sistem peringatan dini berbasis pertanian yang menempatkan keandalan deteksi
sebagai prioritas utama. Berdasarkan rasio biaya tersebut, threshold disesuaikan
dari nilai kuantil 0,98 awal ke nilai yang meminimumkan total expected cost pada
data latih. Penyesuaian ini umumnya menghasilkan threshold yang sedikit lebih
rendah dibandingkan threshold tanpa pertimbangan biaya, sehingga model
menjadi lebih sensitif dalam mendeteksi anomali. Sensitivitas terhadap nilai rasio
biaya dapat dieksplorasi lebih lanjut sebagai bagian dari analisis tambahan pada
Bab 4.
d) Aturan Keputusan dan Pemetaan Severity
Setelah threshold per domain ditentukan untuk setiap model, keputusan deteksi
dilakukan dengan aturan sederhana, yaitu suatu observasi diberi label is_anomaly
= 1 apabila skor model lebih besar atau sama dengan threshold yang berlaku, dan
diberi label is_anomaly = 0 apabila tidak. Aturan ini diterapkan secara seragam
untuk ketiga model (Isolation Forest, Bayesian Network, dan hybrid).
Untuk pemetaan tingkat keparahan, penelitian ini menggunakan pendekatan
post-hoc severity classification, yaitu severity ditentukan setelah keputusan biner
dibuat. Bagi observasi dengan is_anomaly = 0, severity diberi nilai Normal. Bagi
observasi dengan is_anomaly = 1, severity ditentukan berdasarkan magnitude skor
model: kategori Waspada diberikan apabila skor berada di antara threshold dan
kuantil 0,995 dari distribusi skor data latih, sedangkan kategori Bahaya diberikan
apabila skor berada pada atau di atas kuantil 0,995. Pendekatan ini menghasilkan
tiga kategori severity (Normal, Waspada, Bahaya) yang konsisten dengan definisi
pada Subbab 3.5.1, sekaligus memberikan informasi kuantitatif tentang tingkat
keparahan setiap deteksi. Keluaran akhir dari mekanisme ini berupa keputusan
biner anomali, kategori severity, dan skor mentah yang menjadi dasar keputusan.
Ketiga komponen keluaran tersebut akan digunakan sebagai dasar evaluasi kinerja
model pada Subbab 3.5.7, sekaligus menjadi masukan bagi penyusunan tabel fact
alerts yang menjadi keluaran operasional sistem peringatan dini.

62
3.5.7. Evaluasi Model
Evaluasi model dilakukan untuk mengukur kinerja deteksi anomali dari
ketiga model yang dikembangkan, yaitu Isolation Forest, Bayesian Network, dan
model hybrid Isolation Forest–Bayesian Network. Evaluasi dilakukan pada level
keluaran model, yaitu skor dan keputusan biner anomali setelah penerapan threshold
sebagaimana dijelaskan pada Subbab 3.5.6, dengan label biner label_is_anomaly
yang dibentuk pada Subbab 3.5.1 sebagai acuan kebenaran. Evaluasi dirancang agar
memberikan gambaran kinerja yang adil antar model, sekaligus mendukung
perbandingan langsung antara model tunggal dan model hybrid.
a) Skema Pembagian Data
Pembagian data dilakukan secara berbasis waktu (time-based split) untuk
mempertahankan struktur temporal data dan menghindari kebocoran informasi
dari masa depan ke masa lalu pada saat pelatihan. Data periode 1 Januari 2022
hingga 30 Juni 2024 (sekitar 130 minggu) digunakan sebagai data latih, sedangkan
data periode 1 Juli 2024 hingga 31 Desember 2024 (sekitar 26 minggu) digunakan
sebagai data uji. Pembagian ini diterapkan secara konsisten untuk seluruh model
dan seluruh domain risiko.
Pendekatan time-based split dipilih karena lebih sesuai dengan karakteristik
penelitian deteksi risiko yang akan diterapkan pada data baru di masa depan.
Pendekatan ini memastikan bahwa proses pelatihan model dilakukan tanpa
pengetahuan tentang data uji, sehingga estimasi kinerja yang dihasilkan lebih
mencerminkan kemampuan model dalam menghadapi data yang belum pernah
dilihat sebelumnya.
b) Confusion Matrix dan Metrik Klasifikasi
Evaluasi kinerja klasifikasi dilakukan menggunakan confusion matrix sebagai
dasar perhitungan metrik. Confusion matrix memberikan gambaran rinci tentang
jumlah keputusan benar dan salah yang dibuat model, terbagi ke dalam empat
kategori:
(1) True positive (TP), yaitu observasi anomali yang berhasil terdeteksi oleh
model.
(2) True negative (TN), yaitu observasi normal yang dikenali sebagai normal
oleh model.

63
(3) False positive (FP), yaitu observasi normal yang salah dideteksi sebagai
anomali.
(4) False negative (FN), yaitu observasi anomali yang tidak terdeteksi oleh
model.
Berdasarkan keempat kategori tersebut, dihitung tiga metrik klasifikasi utama:
(1) Precision, yaitu proporsi observasi yang dideteksi sebagai anomali dan
benar-benar merupakan anomali. Precision mengukur ketepatan deteksi,
di mana nilai yang lebih tinggi menunjukkan model jarang menghasilkan
alarm palsu.
(2) Recall, yaitu proporsi observasi anomali yang berhasil dideteksi dari
seluruh anomali yang ada. Recall mengukur kelengkapan deteksi, di mana
nilai yang lebih tinggi menunjukkan model jarang melewatkan anomali
nyata.
(3) F1-score, yaitu rata-rata harmonis dari precision dan recall yang
memberikan ukuran keseimbangan antara ketepatan dan kelengkapan
deteksi
c) Receiver Operating Characteristic dan Area Under Curve
Selain metrik klasifikasi pada satu titik threshold, evaluasi juga dilakukan
menggunakan Receiver Operating Characteristic (ROC) dan Area Under Curve
(AUC). Kurva ROC menggambarkan hubungan antara true positive rate dan false
positive rate pada berbagai nilai threshold, sedangkan AUC merangkum kurva
tersebut menjadi satu nilai numerik antara 0 dan 1. Nilai AUC yang lebih tinggi
menunjukkan kemampuan model yang lebih baik dalam membedakan observasi
anomali dan normal pada berbagai threshold, terlepas dari nilai threshold spesifik
yang digunakan.
ROC dan AUC dipilih karena memberikan gambaran kinerja model yang lebih
komprehensif dibandingkan metrik klasifikasi pada satu threshold. Dengan
demikian, evaluasi tidak hanya bergantung pada keputusan deteksi pada nilai
threshold yang dipilih, melainkan juga pada kemampuan model membedakan
kelas pada keseluruhan rentang skor. Hal ini penting untuk membandingkan ketiga
model secara adil, terutama ketika threshold yang digunakan dapat berbeda antar
model.

64
d) Perbandingan Isolation Forest, Bayesian Network, dan Hybrid
Perbandingan kinerja antar model dilakukan untuk mengukur sejauh mana
integrasi pendekatan Isolation Forest dan Bayesian Network melalui feature-level
fusion memberikan peningkatan dibandingkan penggunaan model tunggal.
Perbandingan dilakukan menggunakan kelima metrik di atas, yaitu confusion
matrix, precision, recall, F1-score, dan AUC, pada dua tingkat analisis :
(1) Tingkat global, yaitu kinerja keseluruhan ketiga model pada gabungan
seluruh domain risiko. Perbandingan global memberikan gambaran umum
tentang model mana yang memiliki kinerja terbaik secara menyeluruh.
(2) Tingkat per-domain, yaitu kinerja ketiga model pada setiap domain risiko
(harga, cuaca, OPT, distribusi, tindakan pengelolaan, dan produksi) secara
terpisah. Perbandingan per-domain memungkinkan identifikasi domain
mana yang paling diuntungkan dari pendekatan hybrid, dan domain mana
yang menunjukkan perbedaan kinerja yang lebih kecil antar model.
3.5.8. Kalibrasi, Uncertainty, dan Explainability Model
Selain evaluasi kinerja klasifikasi pada Subbab 3.5.7, penelitian ini juga
menerapkan tiga aspek evaluasi tambahan yang relevan untuk model yang akan
digunakan sebagai komponen sistem peringatan dini, yaitu kalibrasi probabilistik,
uncertainty propagation, dan explainability. Ketiga aspek ini ditujukan untuk
meningkatkan kepercayaan terhadap keluaran model, sehingga probabilitas yang
dihasilkan tidak hanya dapat diukur kinerjanya secara numerik, tetapi juga dapat
ditafsirkan dan dipertanggungjawabkan pada tingkat keputusan operasional.
a) Kalibrasi Probabilistik dengan Brier Score
Kalibrasi probabilistik dilakukan untuk mengukur seberapa baik probabilitas
yang dihasilkan model sesuai dengan frekuensi kejadian sebenarnya. Model
dikatakan terkalibrasi dengan baik apabila probabilitas yang dihasilkan dapat
dipercaya secara langsung; misalnya, observasi yang mendapat probabilitas
anomali sebesar 0,80 sebaiknya benar-benar tergolong anomali pada sekitar 80%
kasus secara historis. Kalibrasi penting untuk model yang akan digunakan secara
operasional, karena operator sistem peringatan dini perlu membandingkan tingkat
keyakinan model dengan keputusan tindakan yang akan diambil.

65
Penelitian ini menggunakan Brier score sebagai metrik kalibrasi utama. Brier
score mengukur rata-rata kuadrat selisih antara probabilitas prediksi dan label
aktual, dengan nilai yang lebih rendah menunjukkan kalibrasi yang lebih baik.
Metrik ini dipilih karena memberikan satu nilai numerik yang merangkum kualitas
kalibrasi keseluruhan dan mudah dibandingkan antar model. Brier score dihitung
untuk ketiga model (Isolation Forest, Bayesian Network, dan hybrid), dan menjadi
indikator pelengkap di samping metrik klasifikasi pada Subbab 3.5.7.
b) Uncertainty Propagation
Uncertainty propagation dilakukan untuk mengukur tingkat ketidakpastian
model terhadap setiap keputusan yang dihasilkan. Pada konteks deteksi anomali,
ketidakpastian penting untuk dipahami karena observasi yang mendekati ambang
keputusan (threshold) cenderung memiliki tingkat keyakinan yang lebih rendah
dibandingkan observasi dengan skor sangat tinggi atau sangat rendah. Informasi
ketidakpastian membantu operator membedakan deteksi yang berasal dari pola
yang sangat jelas dan deteksi yang berada di area abu-abu. Penelitian ini
menggunakan pendekatan uncertainty propagation berbasis Bayesian inference
langsung dari distribusi posterior model Bayesian Network, baik pada model
tunggal maupun pada model hybrid. Pendekatan ini dipilih karena beberapa
alasan:
(1) Konsistensi dengan model, model Bayesian Network secara natural
menghasilkan distribusi probabilitas penuh, sehingga ketidakpastian dapat
diturunkan langsung tanpa transformasi tambahan.
(2) Efisiensi komputasi, pendekatan ini tidak memerlukan pelatihan ulang
model dengan resampling data atau metode bootstrap, sehingga lebih
ringan secara komputasi.
(3) Interpretasi yang langsung, ukuran ketidakpastian yang dihasilkan, seperti
rentang probabilitas atau entropi distribusi posterior, memiliki interpretasi
probabilistik yang jelas dan dapat dilaporkan bersama keputusan deteksi.

66
c) Explainability dengan BN Reasoning
Explainability dilakukan untuk memberikan penjelasan terhadap keputusan
deteksi yang dihasilkan model, sehingga setiap alert yang muncul dapat ditelusuri
kontribusi penyebabnya. Pada sistem peringatan dini, explainability sangat
penting karena keputusan tindakan operasional sering memerlukan justifikasi
yang dapat dipahami oleh pemangku kepentingan, bukan sekadar nilai probabilitas
tanpa konteks. Penelitian ini menggunakan pendekatan Bayesian Network
reasoning sebagai metode explainability, yaitu memanfaatkan struktur DAG dan
Conditional Probability Table (CPT) yang sudah diestimasi pada Subbab 3.5.4
dan 3.5.5 untuk menjelaskan keputusan model. Pendekatan ini dipilih karena
beberapa pertimbangan:
(1) Memanfaatkan struktur model yang sudah ada, tidak diperlukan kerangka
kerja eksternal seperti SHAP, karena struktur probabilistik Bayesian
Network secara natural mendukung penalaran kausal.
(2) Konsisten dengan kerangka inferensi, penjelasan yang dihasilkan
menggunakan logika probabilistik yang sama dengan logika pembuatan
keputusan, sehingga interpretasi tetap koheren.
(3) Sesuai dengan kebutuhan pemangku kepentingan: penjelasan dalam
bentuk kontribusi probabilistik per fitur (misalnya, fitur mana yang paling
memengaruhi probabilitas anomali pada observasi tertentu) lebih mudah
dipahami oleh operator dibandingkan kontribusi numerik abstrak.
d) Integrasi pada Keluaran Model
Ketiga aspek evaluasi tambahan di atas tidak hanya menjadi bagian dari analisis
evaluasi pada Bab 4, tetapi juga diintegrasikan ke dalam keluaran model sebagai
komponen pelengkap. Setiap deteksi yang dihasilkan model akan dilengkapi
dengan tingkat ketidakpastian dari uncertainty propagation dan penjelasan
kontribusi fitur dari Bayesian Network reasoning. Brier score sebagai indikator
kalibrasi dilaporkan pada level keseluruhan model dan per-domain, sehingga
kepercayaan terhadap probabilitas yang dihasilkan dapat diestimasi secara terukur.
Dengan kombinasi evaluasi pada Subbab 3.5.7 dan ketiga aspek evaluasi
tambahan pada subbab ini, model yang dikembangkan diharapkan tidak hanya
menunjukkan kinerja klasifikasi yang baik, tetapi juga memenuhi kebutuhan

67
transparansi dan kepercayaan yang diperlukan untuk implementasi sebagai
komponen sistem peringatan dini pada rantai pasok pertanian.
3.6. Alur Penelitian
Alur penelitian disusun untuk menggambarkan tahapan utama pelaksanaan
penelitian mulai dari identifikasi masalah hingga penarikan kesimpulan. Alur ini
menunjukkan bahwa penelitian dilakukan melalui pengumpulan data sekunder,
pengolahan data multi-domain, pembentukan fitur dan label risiko, pengembangan model
deteksi risiko, serta evaluasi perbandingan performa model. Alur penelitian ditunjukkan
pada Gambar 3.3.
Gambar 3.3 Alur Penelitian
Berdasarkan Gambar 3.3, tahapan penelitian ini adalah sebagai berikut:
a) Identifikasi masalah dan studi literatur
Tahap ini dilakukan untuk mengidentifikasi permasalahan risiko multi-domain
pada rantai pasok pertanian serta memahami keterbatasan pendekatan model
tunggal. Studi literatur digunakan untuk meninjau teori dan penelitian terdahulu
yang relevan dengan anomaly detection, Isolation Forest, Bayesian Network,
model hybrid, dan deteksi risiko pertanian.

68
b) Perumusan masalah, tujuan, dan batasan penelitian
Tahap ini menetapkan rumusan masalah, tujuan penelitian, serta batasan ruang
lingkup agar penelitian tetap terarah. Fokus penelitian diarahkan pada
pengembangan dan evaluasi model hybrid Isolation Forest–Bayesian Network
untuk deteksi risiko multi-domain.
c) Penetapan objek penelitian dan unit analisis
Tahap ini menetapkan objek penelitian berupa deteksi risiko pada rantai pasok
pertanian. Unit analisis yang digunakan adalah observasi mingguan pada level
kecamatan agar data dari berbagai domain dapat dianalisis dalam struktur yang
seragam.
d) Pengumpulan data sekunder
Tahap ini dilakukan dengan mengumpulkan data historis periode 2022–2024 dari
sumber resmi. Data cuaca diperoleh dari BMKG, sedangkan data harga, OPT,
distribusi, tindakan pengelolaan, dan produksi diperoleh dari Dinas Pertanian
Kabupaten Sumedang.
e) Pengolahan data multi-domain
Data yang telah dikumpulkan dikelompokkan ke dalam enam domain risiko, yaitu
harga, cuaca, organisme pengganggu tanaman, distribusi, tindakan pengelolaan,
dan produksi. Pengelompokan ini dilakukan agar karakteristik masing-masing
domain tetap dapat dianalisis secara terpisah.
f) Validasi data dan preprocessing
Tahap ini mencakup pemeriksaan kelayakan data, pembersihan data, penanganan
nilai hilang, normalisasi, dan penyesuaian format data. Proses ini dilakukan agar
data siap digunakan pada tahap pembentukan fitur dan pemodelan.
g) Temporal alignment dan feature engineering
Tahap ini menyelaraskan data dari berbagai resolusi waktu ke dalam unit analisis
mingguan. Setelah itu, dilakukan pembentukan fitur-fitur turunan seperti fitur
dasar, fitur temporal, dan fitur lintas-domain sesuai kebutuhan pemodelan.
h) Pembentukan label risiko

69
Tahap ini dilakukan untuk menghasilkan label risiko yang digunakan sebagai
dasar pelatihan dan evaluasi model. Label risiko dibentuk dalam bentuk label
anomali dan tingkat keparahan risiko.
i) Pengembangan model deteksi risiko
Tahap ini mencakup pengembangan tiga model, yaitu Isolation Forest, Bayesian
Network, dan model hybrid Isolation Forest–Bayesian Network. Isolation Forest
digunakan untuk menghasilkan skor anomali, Bayesian Network digunakan untuk
menghasilkan probabilitas risiko, sedangkan model hybrid mengintegrasikan
keduanya.
j) Thresholding dan keputusan deteksi
Tahap ini mengubah keluaran model menjadi keputusan deteksi berupa kondisi
normal atau anomali. Penentuan keputusan dilakukan menggunakan threshold
yang ditetapkan sesuai karakteristik masing-masing domain.
k) Evaluasi dan perbandingan model
Tahap ini dilakukan untuk menilai dan membandingkan performa Isolation
Forest, Bayesian Network, dan model hybrid. Evaluasi dilakukan menggunakan
metrik yang telah ditentukan, seperti precision, recall, F1-score, dan ROC-AUC.
l) Analisis hasil
Tahap ini dilakukan untuk menginterpretasikan hasil evaluasi model dan
membandingkan karakteristik performa masing-masing pendekatan. Analisis ini
digunakan untuk menilai apakah model hybrid memberikan hasil yang lebih baik
dibandingkan model tunggal.
m) Kesimpulan penelitian
Tahap terakhir adalah merumuskan kesimpulan berdasarkan hasil evaluasi dan
analisis. Kesimpulan disusun untuk menjawab rumusan masalah serta
menunjukkan kontribusi model hybrid dalam deteksi risiko multi-domain pada
rantai pasok pertanian.

70

3.7.  Jadwal Penelitian
Penelitian ini dilaksanakan dalam rentang waktu dari bulan Februari hingga Juli
2026.  Kegiatan  penelitian  disusun  secara  bertahap  mulai  dari  penyusunan  proposal
hingga sidang skripsi. Rincian jadwal pelaksanaan kegiatan penelitian dapat dilihat pada
tabel berikut.
Tabel 3.3  Jadwal Penelitian

| No  Kegiatan Penelitian  | Fase  | Feb  Mar  | Apr  Mei  | Jun  Jul  |     |
| ------------------------ | ----- | --------- | --------- | --------- | --- |

  
| 1  Studi pustaka dan telaah  | Fase  |     |     |     |     |
| ---------------------------- | ----- | --- | --- | --- | --- |

| literatur                    | Persiapan  |       |     |     |     |
| ---------------------------- | ---------- | ----- | --- | --- | --- |
|                              |            |     |    |     |     |
| 2  Penyusunan proposal (Bab  | Fase       |       |     |     |     |
| 1, 2, 3)                     | Persiapan  |       |     |     |     |

| 3  Seminar proposal  | Fase  |     |     |     |     |
| -------------------- | ----- | --- | ---- | --- | --- |

Persiapan
| 4  Pengumpulan dan validasi  | Fase  |     |     |     |     |
| ---------------------------- | ----- | ---- | ---- | --- | --- |
Persiapan
data
| 5  Pengolahan data dan  | Fase          |     |     |     |     |
| ----------------------- | ------------- | --- | ----- | --- | --- |
| pembentukan label       | Implementasi  |     |       |     |     |

| 6   | Fase  |     |     |     |     |
| --- | ----- | --- | --- | --- | --- |
Pengembangan model
Implementasi
| 7   | Fase  |     |     |     |     |
| --- | ----- | --- | --- | ----- | --- |
|     |       |     |     |       |     |
Evaluasi model
Implementasi
| 8   | Fase  |     |     |     |     |
| --- | ----- | --- | --- | ----- | --- |
Penyusunan laporan akhir
Implementasi
| 9   | Fase  |     |     |     |     |
| --- | ----- | --- | --- | ---- | --- |
Sidang akhir
Implementasi

DAFTAR PUSTAKA
[1] Y. Xue, J. Yan, M. Mohsin, and A. Mehak, “Supply chain risks in agri-food
systems: a comprehensive review of economic vulnerabilities and
mitigation approaches,” Front. Sustain. Food Syst., vol. 9, p. 1649834, Nov.
2025, doi: 10.3389/fsufs.2025.1649834.
[2] Y. Zolotnytska et al., “Drivers of Global Wheat and Corn Price Dynamics:
Implications for Sustainable Food Systems,” Sustainability 2025, Vol. 17,
Page 8581, vol. 17, no. 19, p. 8581, Sep. 2025, doi: 10.3390/su17198581.
[3] J. Burney, C. McIntosh, B. Lopez-Videla, K. Samphantharak, and A. G.
Maia, “Empirical modeling of agricultural climate risk,” Proc. Natl. Acad.
Sci. U. S. A., vol. 121, no. 16, p. e2215677121, Apr. 2024, doi:
10.1073/pnas.2215677121.
[4] H. C. Han and D. C. Huang, “Graph-Theoretic Detection of Anomalies in
Supply Chains: A PoR-Based Approach Using Laplacian Flow and Sheaf
Theory,” Mathematics 2025, vol. 13, no. 11, May 2025, doi:
10.3390/math13111795.
[5] Z. Xie, H. Long, C. Ling, Y. Zhou, and Y. Luo, “An anomaly detection
scheme for data stream in cold chain logistics,” PLoS One, vol. 20, no. 3, p.
e0315322, Mar. 2025, doi: 10.1371/journal.pone.0315322.
[6] E. Sediyono, K. D. Hartomo, C. Arthur, I. Utami, R. Prabowo, and R.
Chiong, “An integrated framework for multi-commodity agricultural price
forecasting and anomaly detection using attention-boosted models,” J.
Agric. Food Res., vol. 22, p. 102021, Aug. 2025, doi:
10.1016/j.jafr.2025.102021.
[7] C. Wei, Y. Shan, and M. Z. Zhen, “Deep learning-based anomaly detection
for precision field crop protection,” Front. Plant Sci., vol. 16, p. 1576756,
May 2025, doi: 10.3389/fpls.2025.1576756.
[8] T. J. Krupnik et al., “A weather-forecast driven early warning system for
wheat blast disease: User-centered design, validation, and scaling in
Bangladesh and Brazil,” Clim. Serv., vol. 39, no. 12, p. 100589, Aug. 2025,
doi: 10.1016/j.cliser.2025.100589.
[9] R. Abi, “Bayesian Network Modeling for Probabilistic Reasoning and Risk
Assessment in Large-Scale Industrial Datasets,” International Journal of
Science and Research Archive, vol. 15, no. 3, pp. 587–607, Jun. 2025, doi:
10.30574/ijsra.2025.15.3.1765.
[10] K. Stenhouse et al., “A simulated annealing-based Bayesian network
structure optimization framework for late morbidity prediction with a large
prospective dataset,” Med. Phys., vol. 52, no. 6, pp. 5051–5063, Jun. 2025,
doi: 10.1002/mp.17881.
71

[11] A. Afandi, H. Bedi Agtriadi, and M. Nur Indah Susanti, “Advanced Credit
Scoring with Naive Bayes Algorithm: Improving Accuracy and Reliability
in Financial Risk Assessment,” Jurnal E-Komtek (Elektro-Komputer-
Teknik), vol. 8, no. 2, pp. 399–409, Dec. 2024, doi: 10.37339/e-
komtek.v8i2.2160.
[12] Q. A. Wang, A. W. Lu, Y. Q. Ni, J. F. Wang, and Z. G. Ma, “Bayesian
Network in Structural Health Monitoring: Theoretical Background and
Applications Review,” Sensors 2025, Vol. 25, Page 3577, vol. 25, no. 12, p.
3577, Jun. 2025, doi: 10.3390/s25123577.
[13] N. Babakov, A. Sivaprasad, E. Reiter, and A. Bugarín-Diz, “Reusability of
Bayesian Networks case studies: a survey,” Applied Intelligence 2025 55:6,
vol. 55, no. 6, pp. 417-, Feb. 2025, doi: 10.1007/s10489-025-06289-5.
[14] M. Shanaa and S. Abdallah, “A Hybrid Anomaly Detection Framework
Combining Supervised and Unsupervised Learning for Credit Card Fraud
Detection,” F1000Research 2025 14:664, vol. 14, p. 664, Jul. 2025, doi:
10.12688/f1000research.166350.1.
[15] L. Wang, S. Zhou, T. Zhang, C. Guo, and X. Huang, “An Unsupervised
Anomaly Detection Method for Nuclear Reactor Coolant Pumps Based on
Kernel Self-Organizing Map and Bayesian Posterior Inference,” Energies
2025, Vol. 18, Page 2887, vol. 18, no. 11, p. 2887, May 2025, doi:
10.3390/en18112887.
[16] M. M. Aslam, A. Tufail, L. C. De Silva, and R. A. A. H. M. Apong, “Multi-
Feature Hybrid Anomaly Detection in ICS: An Integration of ML, DL, and
Statistical Techniques,” ACM SecTL 2025 - Proceedings of the 3rd ACM
Workshop on Secure and Trustworthy Deep Learning Systems, Part of ACM
AsiaCCS 2025, vol. 25, pp. 43–51, Aug. 2025, doi:
10.1145/3709021.3737669.
[17] M. Sri Lakshmi, G. Rajavikram, V. Dattatreya, B. Swarna Jyothi, S. Patil,
and M. Bhavsingh, “Evaluating the Isolation Forest Method for Anomaly
Detection in Software-Defined Networking Security,” Journal of Electrical
Systems, vol. 19, no. 4, pp. 279–297, 2023, doi: 10.52783/jes.639.
[18] V. Claudia et al., “ISOLATION FOREST PARAMETER TUNING FOR
MOBILE APP ANOMALY DETECTION BASED ON PERMISSION
REQUESTS,” Jurnal Pilar Nusa Mandiri, vol. 21, no. 2, pp. 187–197, Sep.
2025, doi: 10.33480/pilar.v21i2.6647.
[19] V. Yepmo, G. Smits, M. J. Lesot, and O. Pivert, “CADI: Contextual
Anomaly Detection using an Isolation-Forest,” Proceedings of the ACM
Symposium on Applied Computing, pp. 935–944, Apr. 2024, doi:
10.1145/3605098.3635969.
[20] H. Choi and K. Jung, “Impact of Data Distribution and Bootstrap Setting on
Anomaly Detection Using Isolation Forest in Process Quality Control,”
72

Entropy 2025, Vol. 27, Page 761, vol. 27, no. 7, p. 761, Jul. 2025, doi:
10.3390/e27070761.
[21] A. Entezami, H. Sarmadi, B. Behkamal, and S. Mariani, “Early warning of
structural damage via manifold learning-aided data clustering and non-
parametric probabilistic anomaly detection,” Mech. Syst. Signal Process.,
vol. 224, no. 3, p. 111984, Feb. 2025, doi: 10.1016/j.ymssp.2024.111984.
[22] J. Werner et al., “Enhanced Anomaly Detection for Capsule Endoscopy
Using Ensemble Learning Strategies,” Annu. Int. Conf. IEEE Eng. Med.
Biol. Soc., vol. 2025, pp. 1–7, Jul. 2025, doi:
10.1109/EMBC58623.2025.11253055.
[23] S. Das, S. Shukla, A. S. Kailasam, A. Rai, and A. Chakraborti, “Predicting
and Mitigating Agricultural Price Volatility Using Climate Scenarios and
Risk Models,” Mar. 2025, Accessed: Mar. 08, 2026. [Online]. Available:
http://arxiv.org/abs/2503.24324
[24] K. Wichianrat, P. Chamchang, and Y. Fan, “Risk Identification and
Assessment in Cold Chain Logistics for Durian Exports from Thailand to
China: Insights from Packing House Perspectives,” ABAC Journal, vol. 45,
no. 3, pp. 182–199, Jul. 2025, doi: 10.59865/abacj.2025.22.
[25] R. Shyam, K. Lakra, A. Kumar, and G. Dwivedi, “AI-powered early
warning system for agricultural risk mitigation based on predictive
inference from environmental stress factors and disease propagation
models,” International Journal of Agriculture and Food Science, vol. 7, no.
9, pp. 29–35, Jan. 2025, doi: 10.33545/2664844x.2025.v7.i9a.728.
[26] X. Li et al., “Smart Grain Storage Solution: Integrated Deep Learning
Framework for Grain Storage Monitoring and Risk Alert,” Foods 2025, Vol.
14, Page 1024, vol. 14, no. 6, p. 1024, Mar. 2025, doi:
10.3390/foods14061024.
[27] D. P. Edelson et al., “Early Warning Scores With and Without Artificial
Intelligence,” JAMA Netw. Open, vol. 7, no. 10, pp. e2438986–e2438986,
Oct. 2024, doi: 10.1001/jamanetworkopen.2024.38986.
[28] T. Sim et al., “Prospective external validation of a deep-learning-based
early-warning system for major adverse events in general wards in South
Korea,” Acute and Critical Care, vol. 40, no. 2, pp. 197–208, May 2025,
doi: 10.4266/acc.000525.
[29] D. M. Townsend, R. A. Hunt, and J. Rady, “Chance, probability, and
uncertainty at the edge of human reasoning: What is Knightian
uncertainty?,” Strategic Entrepreneurship Journal, vol. 18, no. 3, pp. 451–
474, Sep. 2024, doi: 10.1002/sej.1516.
[30] A. E. Ebadollahi and S. R. Rahman, “Time-dependent uncertainty
quantification analysis of complex dynamical systems,” 14th International
73

Conference on Structural Safety and Reliability - ICOSSAR’25, May 2025,
doi: 10.23967/icossar.2025.005.
[31] S. Kumari, C. Prabha, A. Karim, M. M. Hassan, and S. Azam, “A
Comprehensive Investigation of Anomaly Detection Methods in Deep
Learning and Machine Learning: 2019–2023,” IET Inf. Secur., vol. 2024,
no. 1, p. 8821891, Jan. 2024, doi: 10.1049/2024/8821891.
[32] N. Mejri, L. Lopez-Fuentes, K. Roy, P. Chernakov, E. Ghorbel, and D.
Aouada, “Unsupervised anomaly detection in time-series: An extensive
evaluation and analysis of state-of-the-art methods,” Expert Syst. Appl., vol.
256, pp. 957–4174, Dec. 2024, doi: 10.1016/j.eswa.2024.124922.
[33] Y. Cao, H. Xiang, H. Zhang, Y. Zhu, and K. M. Ting, “Anomaly Detection
Based on Isolation Mechanisms: A Survey,” Machine Intelligence Research
2025 22:5, vol. 22, no. 5, pp. 849–865, Sep. 2025, doi: 10.1007/s11633-
025-1554-4.
[34] B. Pelletier, “On the statistical properties of the isolation forest anomaly
detection method,” https://doi.org/10.1214/24-EJS2305, vol. 18, no. 2, pp.
4322–4381, Jan. 2024, doi: 10.1214/24-EJS2305.
[35] C. Wei, T. Zhang, C. Li, P. Wang, and Z. Ye, “TAN-FGBMLE: Tree-
Augmented Naive Bayes Structure Learning Based on Fast Generative
Bootstrap Maximum Likelihood Estimation for Continuous-Variable
Classification,” Entropy 2025, Vol. 27, Page 1216, vol. 27, no. 12, p. 1216,
Nov. 2025, doi: 10.3390/e27121216.
[36] F. R. Dastjerdi and L. Cai, “Augmenting Naïve Bayes Classifiers with k-
Tree Topology,” Mathematics 2025, Vol. 13, Page 2185, vol. 13, no. 13, p.
2185, Jul. 2025, doi: 10.3390/math13132185.
[37] E. Richardson, R. Trevizani, J. A. Greenbaum, H. Carter, M. Nielsen, and
B. Peters, “The receiver operating characteristic curve accurately assesses
imbalanced datasets,” Patterns, vol. 5, no. 6, p. 100994, Jun. 2024, doi:
10.1016/j.patter.2024.100994.
[38] W. Chen, K. Yang, Z. Yu, Y. Shi, and C. L. P. Chen, “A survey on
imbalanced learning: latest research, applications and future directions,”
Artif. Intell. Rev., vol. 57, no. 6, pp. 137-, Jun. 2024, doi: 10.1007/s10462-
024-10759-6.
[39] V. Komisarenko and M. Kull, “Cost-sensitive classification with cost
uncertainty: do we need surrogate losses?,” Machine Learning 2025 114:6,
vol. 114, no. 6, pp. 132-, Apr. 2025, doi: 10.1007/s10994-024-06634-8.
74