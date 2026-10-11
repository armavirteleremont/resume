<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Уверен и Готов — ИИ для тех, кто работает руками</title>
    <link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;700&family=Inter:wght@400;600;800&display=swap" rel="stylesheet">
    <style>
        :root {
            --bg-color: #0C3C60;
            --card-bg: #092C44;
            --accent-color: #00FF66;
            --text-color: #FFFFFF;
            --text-muted: #A0B2C6;
        }
        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }
        body {
            font-family: 'Inter', sans-serif;
            background-color: var(--bg-color);
            color: var(--text-color);
            line-height: 1.6;
        }
        .container {
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }
        header, section {
            padding: 50px 20px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }
        h1 {
            font-size: 2.3rem;
            font-weight: 800;
            margin-bottom: 20px;
            line-height: 1.2;
        }
        h2 {
            font-size: 1.6rem;
            margin-bottom: 20px;
            color: var(--accent-color);
            font-family: 'Fira Code', monospace;
        }
        p {
            font-size: 1.1rem;
            color: var(--text-muted);
            margin-bottom: 15px;
        }
        strong {
            color: var(--text-color);
        }
        .hero-subtitle {
            font-size: 1.2rem;
            color: var(--text-color);
            font-weight: 600;
        }
        .terminal-form {
            background: #041420;
            border: 2px solid var(--accent-color);
            padding: 30px;
            border-radius: 6px;
            font-family: 'Fira Code', monospace;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }
        .form-group {
            margin-bottom: 20px;
        }
        .form-group label {
            display: block;
            color: var(--accent-color);
            margin-bottom: 8px;
            font-size: 0.95rem;
        }
        .form-control {
            width: 100%;
            padding: 12px;
            background: var(--card-bg);
            border: 1px solid rgba(0,255,102,0.3);
            color: var(--text-color);
            font-family: 'Fira Code', monospace;
            border-radius: 4px;
            outline: none;
        }
        .form-control:focus {
            border-color: var(--accent-color);
        }
        .btn-terminal {
            background: var(--accent-color);
            color: #000;
            padding: 15px 30px;
            font-weight: 700;
            border: none;
            cursor: pointer;
            font-family: 'Fira Code', monospace;
            width: 100%;
            text-transform: uppercase;
            border-radius: 4px;
            transition: background 0.2s;
        }
        .btn-terminal:hover {
            background: #00cc52;
        }
        .manifest {
            background: var(--card-bg);
            padding: 30px;
            border-radius: 6px;
            border-left: 4px solid var(--accent-color);
        }
        .manifest p {
            margin-bottom: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        
        <!-- Блок 1: Главный экран -->
        <header>
            <h1>ИИ для тех, кто работает руками и головой — 10 часов рутины в неделю без курсов за 50к[cite: 18]</h1>
            <p class="hero-subtitle">«Пока ты занят реальным делом — на верстаке, на объекте или в цеху — алгоритмы работают на тебя»[cite: 18].</p>
        </header>

        <!-- Блок 2: Чистый КПД (Математика времени) -->
        <section>
            <h2>01 // Чистый КПД</h2>
            <p>Пока твои руки заняты паяльником, укладкой кирпича или стрижкой, алгоритмы работают на тебя[cite: 18].</p>
            <p><strong>Результат:</strong> Машина генерирует живые посты для ВК, теги и описания для YouTube и RUTUBE за 0 рублей. Сэкономленные 10 часов рутины возвращаются обратно в бизнес, превращаясь в реальные деньги[cite: 18].</p>
        </section>

        <!-- Блок 3: Инженерный подход (Проблема vs Решение) -->
        <section>
            <h2>02 // Инженерный подход</h2>
            <p><strong>Проблема:</strong> Классические формулы маркетинга (AIDA и прочий пластиковый бред) — это имитация бурной деятельности. Малому бизнесу нужен рабочий инструмент, а не лекции[cite: 18].</p>
            <p><strong>Решение:</strong> Наш инженерный подход. Вместо заумных промптов — жесткие, понятные технические ТЗ. Нейросеть работает как отлаженный осциллограф, выдавая готовый результат за 10 секунд[cite: 18].</p>
        </section>

        <!-- Блок 4: Терминал ввода (Форма подписки) -->
        <section>
            <h2>03 // Терминал ввода</h2>
            <div class="terminal-form">
                <form id="leadForm">
                    <div class="form-group">
                        <label>&gt; ИМЯ:</label>
                        <input type="text" class="form-control" name="name" required placeholder="Введите ваше имя...">
                    </div>
                    <div class="form-group">
                        <label>&gt; КОНТАКТЫ (Телефон / Telegram):</label>
                        <input type="text" class="form-control" name="contacts" required placeholder="@username или телефон...">
                    </div>
                    <div class="form-group">
                        <label>&gt; НИША (Сфера деятельности):</label>
                        <input type="text" class="form-control" name="niche" placeholder="Например: ремонт техники, автосервис...">
                    </div>
                    <button type="submit" class="btn-terminal">[ НАЧАТЬ АВТОМАТИЗАЦИЮ ]</button>
                </form>
            </div>
        </section>

        <!-- Блок 5: Манифест практика -->
        <section>
            <h2>04 // Манифест практика</h2>
            <div class="manifest">
                <p><strong>Автор:</strong> Александр Парфилов[cite: 18]</p>
                <p><strong>Опыт:</strong> 20 лет практического опыта телеремонта (мастерская «Армавиртелеремонт»)[cite: 18].</p>
                <p><em>«Пока твои руки заняты реальным бизнесом и клиентами, машина берет на себя всю рутину. Я не продаю воздух. Я показываю, как скрестить многолетнюю практику на верстаке с ИИ»[cite: 18].</em></p>
            </div>
        </section>

    </div>
</body>
</html>