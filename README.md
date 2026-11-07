# Brique do Bardo

Site de venda de CDs, DVDs e importados usados. Catálogo com busca, filtro por formato e estilo, detalhes de cada item (estado do encarte e da mídia, prensagem, gravadora) e sacola que envia o pedido pelo WhatsApp.

Versões diferentes do mesmo álbum aparecem como itens separados.

## Estrutura

```
index.html          site pronto (gerado; não editar à mão)
src/template.html   layout, estilos e scripts
data/cds.json       catálogo (138 itens)
favicon.svg         "B" da Plakat Fraktur (embutido no index.html)
build.py            junta template + dados + fonte + favicon em index.html
assets/             fonte Plakat Fraktur do título (woff2 embutido no index.html)
```

## Atualizar o catálogo

1. Edite `data/cds.json` (ou peça para gerar a partir da planilha).
2. Rode `python3 build.py`.
3. Faça commit de `data/cds.json` e `index.html`.

Campos de cada item: `banda`, `album`, `ano`, `anoVersao`, `estilo`, `pais`, `versao` (Nacional/Importado), `origem`, `gravadora`, `tipo`, `qtde` (Simples/Duplo/Triplo), `encarte`, `midia`, `obs`, `preco` (número; `0` aparece como "Sob consulta"), `reservado` (`true` bloqueia a compra).

## Publicar no GitHub Pages

Settings → Pages → Source: *Deploy from a branch* → `main` / `(root)`.

---

© 2026 Eduardo Gouvêa · [eduardogouvea.com](https://www.eduardogouvea.com)
