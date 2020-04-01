import matplotlib.pyplot as plt

bact_fasta = (open('bacteria.fasta', 'r').read()).replace('\n', '')
huma_fasta = (open('human.fasta', 'r').read()).replace('\n', '')
covid_txt = open('covid.txt', 'r').read().replace('\n', '')

bact_atcg_cont = dict()
huma_atcg_cont = dict()
covid_atcg_cont = dict()

for letra in ['A', 'T', 'C', 'G']:
    for outra in ['A', 'T', 'C', 'G']:
        bact_atcg_cont[letra+outra] = 0
        huma_atcg_cont[letra+outra] = 0
        covid_atcg_cont[letra+outra] = 0

for c in range(len(bact_fasta)-1):
    bact_atcg_cont[bact_fasta[c]+bact_fasta[c+1]] += 1

for c in range(len(huma_fasta)-1):
    huma_atcg_cont[huma_fasta[c]+huma_fasta[c+1]] += 1

for c in range(len(covid_txt)-1):
    covid_atcg_cont[covid_txt[c]+covid_txt[c+1]] += 1

print('bact', bact_atcg_cont)
print('huma', huma_atcg_cont)
print('covid', covid_atcg_cont)

#html
bact_html = open('bacteria.html', 'w')
c = 1
bact_html.writelines("<h1>Sequência Genética Bacteriana (Escherichia coli)</h1>")
for key in bact_atcg_cont:
    alpha = bact_atcg_cont[key]/max(bact_atcg_cont.values())
    bact_html.writelines(f"<div style='float:left; text-align: center; width: 100px; height: 100px; border: 1px solid #111; background-color: rgba(255, 0, 0, {alpha});'>{key}</div>\n")

    if c%4 == 0:
        bact_html.writelines("<div style='clear: both;'></div>")

    c += 1

bact_html.writelines(f"<p>{open('bacteria.fasta', 'r').read()}</p>")
bact_html.close()

###
huma_html = open('human.html', 'w')
c = 1
huma_html.writelines("<h1>Sequência Genética Humana</h1>")
for key in huma_atcg_cont:
    alpha = huma_atcg_cont[key]/max(huma_atcg_cont.values())
    huma_html.writelines(f"<div style='float:left; text-align: center; width: 100px; height: 100px; border: 1px solid #111; background-color: rgba(255, 0, 0, {alpha});'>{key}</div>\n")

    if c%4 == 0:
        huma_html.writelines("<div style='clear: both;'></div>")

    c += 1

huma_html.writelines(f"<p>{open('human.fasta', 'r').read()}</p>")
huma_html.close()

###
covid_html = open('covid19.html', 'w')
c = 1
covid_html.writelines("<h1>Sequência Genética SARS-CoV-2</h1>")
for key in covid_atcg_cont:
    alpha = covid_atcg_cont[key]/max(covid_atcg_cont.values())
    covid_html.writelines(f"<div style='float:left; text-align: center; width: 100px; height: 100px; border: 1px solid #111; background-color: rgba(255, 0, 0, {alpha});'>{key}</div>\n")

    if c%4 == 0:
        covid_html.writelines("<div style='clear: both;'></div>")

    c += 1

covid_html.writelines(f"<p>{open('covid.txt', 'r').read()}</p>")
covid_html.close()

####
rna_comp_html = open('rna_comp.html', 'w')
bact_html_cont = open('bacteria.html', 'r').read()
huma_html_cont = open('human.html', 'r').read()
covid_html_cont = open('covid19.html', 'r').read()
rna_comp_html.write(f"{bact_html_cont}\n\n\n{huma_html_cont}\n\n\n{covid_html_cont}")
rna_comp_html.close()
