# Transformações de Intensidade em Imagens

## 1. Alargamento de Contraste
O **alargamento de contraste** redistribui os níveis de intensidade da imagem para ocupar uma faixa maior (normalmente [0,255] ou [0,1]).  
- Intervalos como 2–98%, 5–95% ou 10–90% determinam quanto das intensidades extremas são descartadas.  
- Quanto menor a faixa, maior o contraste no miolo, mas mais detalhes nas sombras e brilhos são sacrificados.  

---

## 2. Negativo
O **negativo** inverte os níveis de intensidade:  
- Fórmula em float: `s = 1 - r`.  
- Fórmula em uint8: `s = 255 - r`.  
Tudo o que era claro vira escuro e vice-versa.  

---

## 3. Transformação Logarítmica
A **transformação logarítmica** é dada por:  
\[
s = c \cdot \log(1 + r)
\]  
- Realça **regiões escuras** (expande tons baixos).  
- Comprime **regiões claras** (reduz saturação nos brancos).  
- O parâmetro *gain (c)* controla a intensidade do efeito.  

---

## 4. Transformação Potência (Gamma)
A **transformação potência (gamma)** é dada por:  
\[
s = r^\gamma
\]  
- Se **γ < 1**: clareia a imagem (expande tons escuros).  
- Se **γ = 1**: mantém a imagem inalterada.  
- Se **γ > 1**: escurece a imagem (expande tons claros).  
- Usada em correção de brilho/contraste e ajuste de monitores.  
