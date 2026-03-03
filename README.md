# 🎯 Colisão de Objetos com Condições de Contorno

Simulação desenvolvida em **Python 3.12** utilizando **Pygame**, demonstrando colisão entre dois objetos (`Rect`) com tratamento de condições de contorno em ambiente 2D.

📚 **Disciplina:** Computação Gráfica e Tecnologias Imersivas (SINF7NA)  
👨‍🏫 **Professor:** Dr. Rafael Barbosa  

---

## 📌 Objetivo da Atividade

Desenvolver uma aplicação gráfica que implemente:

- Dois objetos (`Rect`) em movimento contínuo  
- Detecção de colisão entre objetos  
- Colisão com as bordas da janela  
- Alteração dinâmica de direção  
- Mudança de cor após colisão  
- Organização e versionamento com Git e GitHub  

---

## 🧠 Conceitos Aplicados

Durante o desenvolvimento foram aplicados os seguintes conceitos:

- Estrutura de **Game Loop**
- Programação orientada a eventos
- Manipulação de vetores de velocidade (eixos X e Y)
- Implementação de condições de contorno
- Detecção de colisão com `colliderect()`
- Renderização de texto em tempo real
- Controle de FPS com `Clock`

---

## ⚙️ Tecnologias Utilizadas

- Python 3.12  
- Pygame  

---

## 📂 Estrutura do Projeto

```
pygame/
│
├── venv311/
├── README.md
└── teste-pygame.py
```

---

# 🏗 Estrutura do Código Explicada

## 1️⃣ Inicialização do Pygame

```python
pygame.init()

largura = 800
altura = 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Janela")
```

Nesta etapa:

- Inicializa-se o Pygame  
- Define-se o tamanho da janela  
- Cria-se a superfície principal de renderização  

---

## 2️⃣ Criação dos Objetos (Surface e Rect)

```python
texto = fonte.render("Vitor", True, BRANCO)
texto_rect = texto.get_rect()
```

Cada texto possui:

- Uma `Surface` (representação visual)
- Um `Rect` (posição e área de colisão)

O `Rect` é responsável por:

- Detectar colisões  
- Definir limites  
- Atualizar posição  

---

## 3️⃣ Velocidade Aleatória Inicial

```python
velocidade_x = random.randint(-2, 2)
velocidade_y = random.randint(-2, 2)
```

Evita-se velocidade `(0,0)` para impedir que o objeto permaneça parado:

```python
while velocidade_x == 0 and velocidade_y == 0:
    velocidade_x = random.randint(-2, 2)
    velocidade_y = random.randint(-2, 2)
```

Movimentação baseada em:

```
posição += velocidade
```

---

## 4️⃣ Game Loop (Loop Principal)

```python
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
```

O loop principal é responsável por:

- Capturar eventos  
- Atualizar posições  
- Verificar colisões  
- Renderizar elementos  
- Atualizar a tela  

Esse modelo é padrão no desenvolvimento de jogos e simulações gráficas.

---

## 5️⃣ Movimento dos Objetos

```python
texto_rect.x += velocidade_x
texto_rect.y += velocidade_y
```

A posição do objeto é atualizada continuamente com base em sua velocidade.

---

## 6️⃣ Condições de Contorno (Colisão com Bordas)

Exemplo:

```python
if texto_rect.right >= largura:
    texto_rect.right = largura
    velocidade_x = random.randint(-2, 0)
```

Quando o objeto atinge uma borda:

- A posição é corrigida  
- A direção é alterada  
- Uma nova velocidade é atribuída  

Isso simula o efeito clássico semelhante ao protetor de tela DVD.

---

## 7️⃣ Colisão Entre Objetos

```python
if rect1.colliderect(rect2):
    velocidade_x1 = random.randint(-2, 2)
    velocidade_y1 = random.randint(-2, 2)
    velocidade_x2 = random.randint(-2, 2)
    velocidade_y2 = random.randint(-2, 2)
```

Quando ocorre colisão:

- Ambos os objetos recebem novas velocidades  
- A direção do movimento é alterada  

---

## 8️⃣ Alteração Dinâmica de Cor

```python
cor = (
    random.randint(1, 255),
    random.randint(1, 255),
    random.randint(1, 255)
)
```

Após a colisão:

- Uma nova cor RGB é gerada  
- O texto é renderizado novamente com a nova cor  

---

## 9️⃣ Controle de FPS

```python
clock.tick(240)
```

Limita a execução a 240 quadros por segundo, garantindo:

- Estabilidade  
- Fluidez  
- Controle do processamento  

---

# ▶️ Como Executar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/Vitor-Medeiros/pygame
cd pygame
```

### 2️⃣ Instalar o Pygame

```bash
pip install pygame
```

### 3️⃣ Executar o projeto

```bash
python teste-pygame.py
```

---

# 🎮 Funcionamento da Simulação

- Dois textos movimentam-se continuamente pela tela  
- Ao colidir com as bordas:
  - A direção é ajustada  
- Ao colidir entre si:
  - Novas velocidades são atribuídas  
  - A cor é alterada dinamicamente  
- O comportamento é dinâmico e não determinístico  

A simulação demonstra, de forma prática, conceitos fundamentais de **computação gráfica**, **movimento bidimensional** e **detecção de colisão em tempo real**.