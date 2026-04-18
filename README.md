<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Nicoli Felipe — Data Scientist</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@0,300;0,400;0,500;0,700;1,400&family=Syne:wght@400;500;700;800&display=swap" rel="stylesheet">
<style>
  :root {
    --bg: #0a0c10;
    --bg2: #0f1117;
    --bg3: #161b22;
    --bg4: #1c2333;
    --border: rgba(255,255,255,0.07);
    --border2: rgba(255,255,255,0.13);
    --text: #e6edf3;
    --muted: #7d8590;
    --accent: #58a6ff;
    --accent2: #3fb950;
    --accent3: #f78166;
    --accent4: #d2a8ff;
    --accent5: #ffa657;
    --glow: rgba(88,166,255,0.12);
  }


  * { margin: 0; padding: 0; box-sizing: border-box; }


  body {
    background: var(--bg);
    color: var(--text);
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    line-height: 1.7;
    min-height: 100vh;
    overflow-x: hidden;
  }


  /* GRID BACKGROUND */
  body::before {
    content: '';
    position: fixed;
    inset: 0;
    background-image:
      linear-gradient(rgba(88,166,255,0.03) 1px, transparent 1px),
      linear-gradient(90deg, rgba(88,166,255,0.03) 1px, transparent 1px);
    background-size: 40px 40px;
    pointer-events: none;
    z-index: 0;
  }


  .container {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 24px;
    position: relative;
    z-index: 1;
  }


  /* NAV */
  nav {
    border-bottom: 1px solid var(--border);
    padding: 16px 0;
    background: rgba(10,12,16,0.8);
    backdrop-filter: blur(8px);
    position: sticky;
    top: 0;
    z-index: 100;
  }


  nav .container {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }


  .nav-logo {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 16px;
    letter-spacing: -0.5px;
    color: var(--text);
  }


  .nav-logo span { color: var(--accent); }


  .nav-links {
    display: flex;
    gap: 24px;
    list-style: none;
  }


  .nav-links a {
    color: var(--muted);
    text-decoration: none;
    font-size: 12px;
    letter-spacing: 0.5px;
    transition: color 0.2s;
  }


  .nav-links a:hover { color: var(--accent); }


  /* HERO */
  .hero {
    padding: 80px 0 60px;
  }


  .hero-prompt {
    font-size: 11px;
    color: var(--accent);
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-bottom: 20px;
    opacity: 0.7;
  }


  .hero-prompt::before { content: '$ '; color: var(--accent2); }


  .hero-name {
    font-family: 'Syne', sans-serif;
    font-size: clamp(42px, 7vw, 72px);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -2px;
    margin-bottom: 8px;
    background: linear-gradient(135deg, #e6edf3 0%, #58a6ff 60%, #d2a8ff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }


  .hero-role {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 400;
    color: var(--muted);
    margin-bottom: 28px;
  }


  .hero-role .highlight {
    color: var(--accent2);
    font-weight: 500;
  }


  .hero-bio {
    max-width: 580px;
    color: #8b949e;
    font-size: 13px;
    line-height: 1.8;
    margin-bottom: 32px;
    font-family: 'JetBrains Mono', monospace;
  }


  .hero-bio .comment { color: #484f58; }


  .hero-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
    margin-bottom: 36px;
  }


  .tag {
    font-size: 11px;
    padding: 4px 12px;
    border-radius: 20px;
    border: 1px solid var(--border2);
    color: var(--muted);
    letter-spacing: 0.5px;
  }


  .tag.blue { border-color: rgba(88,166,255,0.3); color: var(--accent); }
  .tag.green { border-color: rgba(63,185,80,0.3); color: var(--accent2); }
  .tag.purple { border-color: rgba(210,168,255,0.3); color: var(--accent4); }
  .tag.orange { border-color: rgba(255,166,87,0.3); color: var(--accent5); }


  .cta-row {
    display: flex;
    gap: 12px;
    flex-wrap: wrap;
  }


  .btn {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    padding: 10px 20px;
    border-radius: 6px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    text-decoration: none;
    transition: all 0.2s;
    letter-spacing: 0.3px;
  }


  .btn-primary {
    background: var(--accent);
    color: #0a0c10;
    font-weight: 700;
  }


  .btn-primary:hover { background: #79c0ff; }


  .btn-secondary {
    border: 1px solid var(--border2);
    color: var(--muted);
  }


  .btn-secondary:hover { border-color: var(--accent); color: var(--accent); }


  /* STATUS BAR */
  .status-bar {
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 14px 20px;
    display: flex;
    align-items: center;
    gap: 12px;
    background: var(--bg2);
    margin-bottom: 64px;
    font-size: 12px;
    color: var(--muted);
  }


  .status-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: var(--accent2);
    box-shadow: 0 0 6px var(--accent2);
    flex-shrink: 0;
    animation: pulse 2s infinite;
  }


  @keyframes pulse {
    0%, 100% { opacity: 1; }
    50% { opacity: 0.4; }
  }


  /* SECTION */
  .section { margin-bottom: 72px; }


  .section-header {
    display: flex;
    align-items: center;
    gap: 12px;
    margin-bottom: 28px;
  }


  .section-label {
    font-size: 10px;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: var(--accent);
    font-weight: 500;
  }


  .section-line {
    flex: 1;
    height: 1px;
    background: var(--border);
  }


  /* STATS GRID */
  .stats-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin-bottom: 48px;
  }


  .stat-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px;
    transition: border-color 0.2s;
  }


  .stat-card:hover { border-color: var(--border2); }


  .stat-number {
    font-family: 'Syne', sans-serif;
    font-size: 32px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1;
    margin-bottom: 4px;
  }


  .stat-label {
    font-size: 11px;
    color: var(--muted);
    letter-spacing: 0.5px;
  }


  /* SKILLS */
  .skills-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
  }


  .skill-group {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 24px;
    transition: border-color 0.2s, background 0.2s;
  }


  .skill-group:hover {
    border-color: var(--border2);
    background: var(--bg3);
  }


  .skill-group-title {
    font-size: 11px;
    letter-spacing: 2px;
    text-transform: uppercase;
    color: var(--muted);
    margin-bottom: 14px;
    display: flex;
    align-items: center;
    gap: 8px;
  }


  .skill-group-title::before {
    content: '';
    width: 6px; height: 6px;
    border-radius: 50%;
    background: currentColor;
    flex-shrink: 0;
  }


  .skill-group.data .skill-group-title { color: var(--accent); }
  .skill-group.ai .skill-group-title { color: var(--accent4); }
  .skill-group.tools .skill-group-title { color: var(--accent2); }
  .skill-group.soft .skill-group-title { color: var(--accent5); }


  .skill-items {
    display: flex;
    flex-wrap: wrap;
    gap: 6px;
  }


  .skill-pill {
    font-size: 11px;
    padding: 3px 10px;
    border-radius: 4px;
    background: rgba(255,255,255,0.04);
    color: #8b949e;
    border: 1px solid var(--border);
    font-family: 'JetBrains Mono', monospace;
  }


  /* EXPERIENCE */
  .exp-list { display: flex; flex-direction: column; gap: 0; }


  .exp-item {
    display: grid;
    grid-template-columns: 1px 1fr;
    gap: 0 24px;
    padding-bottom: 32px;
  }


  .exp-item:last-child { padding-bottom: 0; }


  .exp-line-col {
    display: flex;
    flex-direction: column;
    align-items: center;
  }


  .exp-dot {
    width: 10px; height: 10px;
    border-radius: 50%;
    border: 2px solid var(--accent);
    background: var(--bg);
    flex-shrink: 0;
    margin-top: 4px;
    z-index: 1;
  }


  .exp-vline {
    flex: 1;
    width: 1px;
    background: var(--border);
    margin-top: 6px;
  }


  .exp-item:last-child .exp-vline { display: none; }


  .exp-content { padding-bottom: 4px; }


  .exp-header {
    display: flex;
    align-items: flex-start;
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 4px;
    flex-wrap: wrap;
  }


  .exp-title {
    font-family: 'Syne', sans-serif;
    font-size: 15px;
    font-weight: 700;
    color: var(--text);
  }


  .exp-company {
    color: var(--accent);
    font-size: 12px;
    margin-bottom: 4px;
  }


  .exp-meta {
    font-size: 11px;
    color: var(--muted);
    white-space: nowrap;
  }


  .exp-desc {
    font-size: 12px;
    color: #8b949e;
    line-height: 1.8;
    margin-top: 8px;
  }


  .exp-bullets {
    list-style: none;
    margin-top: 8px;
  }


  .exp-bullets li {
    font-size: 12px;
    color: #8b949e;
    padding: 2px 0;
    padding-left: 16px;
    position: relative;
    line-height: 1.7;
  }


  .exp-bullets li::before {
    content: '→';
    position: absolute;
    left: 0;
    color: var(--accent2);
    font-size: 10px;
    top: 4px;
  }


  /* EDUCATION */
  .edu-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 16px;
  }


  .edu-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 20px 24px;
    transition: border-color 0.2s;
  }


  .edu-card:hover { border-color: var(--border2); }


  .edu-degree {
    font-family: 'Syne', sans-serif;
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 4px;
    color: var(--text);
  }


  .edu-school {
    font-size: 12px;
    color: var(--accent);
    margin-bottom: 4px;
  }


  .edu-detail {
    font-size: 11px;
    color: var(--muted);
  }


  /* FEATURED SECTION */
  .featured-card {
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 28px 32px;
    position: relative;
    overflow: hidden;
  }


  .featured-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--accent), var(--accent4));
  }


  .featured-title {
    font-family: 'Syne', sans-serif;
    font-size: 18px;
    font-weight: 700;
    margin-bottom: 8px;
    color: var(--text);
  }


  .featured-subtitle {
    font-size: 12px;
    color: var(--muted);
    margin-bottom: 16px;
  }


  .featured-desc {
    font-size: 13px;
    color: #8b949e;
    line-height: 1.8;
    max-width: 600px;
  }


  .research-tag {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    font-size: 10px;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    color: var(--accent4);
    padding: 4px 10px;
    border: 1px solid rgba(210,168,255,0.2);
    border-radius: 4px;
    margin-bottom: 16px;
  }


  /* LANG */
  .lang-row {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
  }


  .lang-item {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--bg2);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 12px 18px;
  }


  .lang-name {
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    font-size: 14px;
  }


  .lang-level {
    font-size: 11px;
    color: var(--muted);
  }


  .lang-bar {
    width: 60px;
    height: 3px;
    background: var(--border);
    border-radius: 3px;
    overflow: hidden;
  }


  .lang-fill {
    height: 100%;
    border-radius: 3px;
    background: var(--accent);
  }


  /* FOOTER */
  footer {
    border-top: 1px solid var(--border);
    padding: 32px 0;
    margin-top: 48px;
  }


  .footer-inner {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    flex-wrap: wrap;
  }


  .footer-copy {
    font-size: 11px;
    color: var(--muted);
  }


  .footer-links {
    display: flex;
    gap: 20px;
  }


  .footer-links a {
    font-size: 11px;
    color: var(--muted);
    text-decoration: none;
    transition: color 0.2s;
  }


  .footer-links a:hover { color: var(--accent); }


  /* ANIMATIONS */
  @keyframes fadeInUp {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
  }


  .hero { animation: fadeInUp 0.6s ease both; }
  .hero-prompt { animation: fadeInUp 0.6s 0.1s ease both; }


  /* CODE BLOCK STYLE */
  .code-block {
    background: var(--bg3);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 16px 20px;
    font-size: 12px;
    color: var(--muted);
    margin-top: 24px;
    overflow-x: auto;
    white-space: pre;
  }


  .code-block .k { color: var(--accent4); }
  .code-block .s { color: var(--accent2); }
  .code-block .c { color: #484f58; }
  .code-block .f { color: var(--accent); }
  .code-block .n { color: var(--accent5); }


  /* SCROLLBAR */
  ::-webkit-scrollbar { width: 8px; }
  ::-webkit-scrollbar-track { background: var(--bg); }
  ::-webkit-scrollbar-thumb { background: var(--bg4); border-radius: 4px; }
  ::-webkit-scrollbar-thumb:hover { background: var(--muted); }
</style>
</head>
<body>


<!-- NAV -->
<nav>
  <div class="container">
    <div class="nav-logo">nicoli<span>.</span>felipe</div>
    <ul class="nav-links">
      <li><a href="#about">about</a></li>
      <li><a href="#skills">skills</a></li>
      <li><a href="#experience">experience</a></li>
      <li><a href="#education">education</a></li>
      <li><a href="mailto:nicolifelipe01@gmail.com">contact</a></li>
    </ul>
  </div>
</nav>


<!-- HERO -->
<main>
<div class="container">


  <section class="hero" id="about">
    <p class="hero-prompt">whoami</p>
    <h1 class="hero-name">Nicoli<br>Felipe</h1>
    <p class="hero-role"><span class="highlight">Data Scientist</span> &amp; BI Analyst · São Paulo, BR</p>


    <p class="hero-bio">
<span class="comment">// turning raw data into decisions</span>
Passionate about the intersection of data, AI, and business intelligence.
Currently pursuing a dual degree in Data Science (SENAI) and
Business IT (FATEC), building a foundation across the full
data pipeline — from collection to insight.
    </p>


    <div class="hero-tags">
      <span class="tag blue">Python</span>
      <span class="tag blue">SQL</span>
      <span class="tag blue">Power BI</span>
      <span class="tag green">Machine Learning</span>
      <span class="tag green">EDA</span>
      <span class="tag purple">AI Prompt Engineering</span>
      <span class="tag purple">Industry 5.0</span>
      <span class="tag orange">KPIs &amp; Reporting</span>
      <span class="tag orange">Agile</span>
    </div>


    <div class="cta-row">
      <a href="https://www.linkedin.com/in/nicoli-felipe/" target="_blank" class="btn btn-primary">↗ LinkedIn</a>
      <a href="mailto:nicolifelipe01@gmail.com" class="btn btn-secondary">✉ Get in touch</a>
    </div>


    <div class="code-block"><span class="c"># nicoli_felipe.py</span>


<span class="k">class</span> <span class="f">NicoliFelipe</span>:
    focus     = <span class="s">"Data Science · BI · AI Research"</span>
    location  = <span class="s">"São Paulo, Brasil 🇧🇷"</span>
    learning  = [<span class="s">"Statistical Modeling"</span>, <span class="s">"Deep Learning"</span>, <span class="s">"MLOps"</span>]
    languages = {<span class="s">"Python"</span>: <span class="s">"🔥"</span>, <span class="s">"SQL"</span>: <span class="s">"⚡"</span>, <span class="s">"Portuguese"</span>: <span class="s">"native"</span>}
    open_to   = [<span class="s">"internships"</span>, <span class="s">"research"</span>, <span class="s">"data projects"</span>]</div>


    <div class="status-bar" style="margin-top:24px; margin-bottom:0;">
      <div class="status-dot"></div>
      <span>Currently: Operations Intern @ Fenix Systems · Open to new data opportunities</span>
    </div>
  </section>


  <!-- STATS -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">at a glance</span>
      <div class="section-line"></div>
    </div>
    <div class="stats-grid">
      <div class="stat-card">
        <div class="stat-number" style="color: var(--accent);">4,320</div>
        <div class="stat-label">hours of formal training</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color: var(--accent2);">5+</div>
        <div class="stat-label">roles & internships</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color: var(--accent4);">3</div>
        <div class="stat-label">languages spoken</div>
      </div>
      <div class="stat-card">
        <div class="stat-number" style="color: var(--accent5);">2</div>
        <div class="stat-label">degrees in progress</div>
      </div>
    </div>
  </section>


  <!-- SKILLS -->
  <section class="section" id="skills">
    <div class="section-header">
      <span class="section-label">skills</span>
      <div class="section-line"></div>
    </div>
    <div class="skills-grid">
      <div class="skill-group data">
        <div class="skill-group-title">Data &amp; Analytics</div>
        <div class="skill-items">
          <span class="skill-pill">Python</span>
          <span class="skill-pill">SQL</span>
          <span class="skill-pill">Power BI</span>
          <span class="skill-pill">Excel</span>
          <span class="skill-pill">Statistics</span>
          <span class="skill-pill">EDA</span>
          <span class="skill-pill">KPI Design</span>
          <span class="skill-pill">Data Validation</span>
        </div>
      </div>
      <div class="skill-group ai">
        <div class="skill-group-title">AI &amp; Research</div>
        <div class="skill-items">
          <span class="skill-pill">Prompt Engineering</span>
          <span class="skill-pill">AI Evaluation</span>
          <span class="skill-pill">Web Scraping</span>
          <span class="skill-pill">API Integration</span>
          <span class="skill-pill">Industry 5.0</span>
          <span class="skill-pill">Scientific Writing</span>
        </div>
      </div>
      <div class="skill-group tools">
        <div class="skill-group-title">Project &amp; Process</div>
        <div class="skill-items">
          <span class="skill-pill">Agile / Scrum</span>
          <span class="skill-pill">Canvas</span>
          <span class="skill-pill">QA Testing</span>
          <span class="skill-pill">Documentation</span>
          <span class="skill-pill">Reporting</span>
          <span class="skill-pill">Requirements Mapping</span>
        </div>
      </div>
      <div class="skill-group soft">
        <div class="skill-group-title">Behavioral</div>
        <div class="skill-items">
          <span class="skill-pill">Analytical Thinking</span>
          <span class="skill-pill">Communication</span>
          <span class="skill-pill">Leadership</span>
          <span class="skill-pill">Feedback</span>
          <span class="skill-pill">Continuous Learning</span>
        </div>
      </div>
    </div>
  </section>


   <!-- EDUCATION -->
  <section class="section" id="education">
    <div class="section-header">
      <span class="section-label">education</span>
      <div class="section-line"></div>
    </div>
    <div class="edu-grid">
      <div class="edu-card">
        <div class="edu-degree">Associate Degree in Data Science</div>
        <div class="edu-school">SENAI</div>
        <div class="edu-detail">2,320 h · Jan 2025 – Dec 2026</div>
      </div>
      <div class="edu-card">
        <div class="edu-degree">Associate Degree in Business IT</div>
        <div class="edu-school">FATEC</div>
        <div class="edu-detail">2,800 h · Feb 2025 – Dec 2028</div>
      </div>
      <div class="edu-card">
        <div class="edu-degree">Technical Program in Administration</div>
        <div class="edu-school">ETEC</div>
        <div class="edu-detail">1,200 h · Jul 2023 – Dec 2024</div>
      </div>
    </div>


    <!-- Courses -->
    <div style="margin-top: 20px;">
      <p style="font-size: 11px; color: var(--muted); letter-spacing: 1px; text-transform: uppercase; margin-bottom: 12px;">complementary courses</p>
      <div style="display: flex; flex-wrap: wrap; gap: 8px;">
        <span class="tag">Python · 80h</span>
        <span class="tag">Power BI · 20h</span>
        <span class="tag">Excel · 160h</span>
        <span class="tag">HR Assistant · 160h</span>
        <span class="tag">Quality Tools · 40h</span>
        <span class="tag">Advanced Programming · 15h</span>
        <span class="tag">Computer Skills · 80h</span>
      </div>
    </div>
  </section>


  <!-- LANGUAGES -->
  <section class="section">
    <div class="section-header">
      <span class="section-label">languages</span>
      <div class="section-line"></div>
    </div>
    <div class="lang-row">
      <div class="lang-item">
        <div>
          <div class="lang-name">Português</div>
          <div class="lang-level">Native</div>
        </div>
        <div class="lang-bar"><div class="lang-fill" style="width:100%; background: var(--accent2);"></div></div>
      </div>
      <div class="lang-item">
        <div>
          <div class="lang-name">English</div>
          <div class="lang-level">Intermediate</div>
        </div>
        <div class="lang-bar"><div class="lang-fill" style="width:60%;"></div></div>
      </div>
      <div class="lang-item">
        <div>
          <div class="lang-name">Español</div>
          <div class="lang-level">Basic</div>
        </div>
        <div class="lang-bar"><div class="lang-fill" style="width:25%; background: var(--accent5);"></div></div>
      </div>
    </div>
  </section>


</div>
</main>


<!-- FOOTER -->
<footer>
  <div class="container">
    <div class="footer-inner">
      <span class="footer-copy">© 2025 Nicoli Felipe · São Paulo, Brasil</span>
      <div class="footer-links">
        <a href="https://www.linkedin.com/in/nicoli-felipe/" target="_blank">LinkedIn</a>
        <a href="mailto:nicolifelipe01@gmail.com">Email</a>
      </div>
    </div>
  </div>
</footer>


</body>
</html>



