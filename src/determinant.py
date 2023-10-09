all_langs = {
    "TGLANG_LANGUAGE_OTHER",
    "TGLANG_LANGUAGE_1S_ENTERPRISE",
    "TGLANG_LANGUAGE_ABAP",
    "TGLANG_LANGUAGE_ACTIONSCRIPT",
    "TGLANG_LANGUAGE_ADA",
    "TGLANG_LANGUAGE_APACHE_GROOVY",
    "TGLANG_LANGUAGE_APEX",
    "TGLANG_LANGUAGE_APPLESCRIPT",
    "TGLANG_LANGUAGE_ASP",
    "TGLANG_LANGUAGE_ASSEMBLY",
    "TGLANG_LANGUAGE_AUTOHOTKEY",
    "TGLANG_LANGUAGE_AWK",
    "TGLANG_LANGUAGE_BASIC",
    "TGLANG_LANGUAGE_BATCH",
    "TGLANG_LANGUAGE_BISON",
    "TGLANG_LANGUAGE_C",
    "TGLANG_LANGUAGE_CLOJURE",
    "TGLANG_LANGUAGE_CMAKE",
    "TGLANG_LANGUAGE_COBOL",
    "TGLANG_LANGUAGE_COFFESCRIPT",
    "TGLANG_LANGUAGE_COMMON_LISP",
    "TGLANG_LANGUAGE_CPLUSPLUS",
    "TGLANG_LANGUAGE_CRYSTAL",
    "TGLANG_LANGUAGE_CSHARP",
    "TGLANG_LANGUAGE_CSS",
    "TGLANG_LANGUAGE_CSV",
    "TGLANG_LANGUAGE_D",
    "TGLANG_LANGUAGE_DART",
    "TGLANG_LANGUAGE_DELPHI",
    "TGLANG_LANGUAGE_DOCKER",
    "TGLANG_LANGUAGE_ELIXIR",
    "TGLANG_LANGUAGE_ELM",
    "TGLANG_LANGUAGE_ERLANG",
    "TGLANG_LANGUAGE_FIFT",
    "TGLANG_LANGUAGE_FORTH",
    "TGLANG_LANGUAGE_FORTRAN",
    "TGLANG_LANGUAGE_FSHARP",
    "TGLANG_LANGUAGE_FUNC",
    "TGLANG_LANGUAGE_GAMS",
    "TGLANG_LANGUAGE_GO",
    "TGLANG_LANGUAGE_GRADLE",
    "TGLANG_LANGUAGE_GRAPHQL",
    "TGLANG_LANGUAGE_HACK",
    "TGLANG_LANGUAGE_HASKELL",
    "TGLANG_LANGUAGE_HTML",
    "TGLANG_LANGUAGE_ICON",
    "TGLANG_LANGUAGE_IDL",
    "TGLANG_LANGUAGE_INI",
    "TGLANG_LANGUAGE_JAVA",
    "TGLANG_LANGUAGE_JAVASCRIPT",
    "TGLANG_LANGUAGE_JSON",
    "TGLANG_LANGUAGE_JULIA",
    "TGLANG_LANGUAGE_KEYMAN",
    "TGLANG_LANGUAGE_KOTLIN",
    "TGLANG_LANGUAGE_LATEX",
    "TGLANG_LANGUAGE_LISP",
    "TGLANG_LANGUAGE_LOGO",
    "TGLANG_LANGUAGE_LUA",
    "TGLANG_LANGUAGE_MAKEFILE",
    "TGLANG_LANGUAGE_MARKDOWN",
    "TGLANG_LANGUAGE_MATLAB",
    "TGLANG_LANGUAGE_NGINX",
    "TGLANG_LANGUAGE_NIM",
    "TGLANG_LANGUAGE_OBJECTIVE_C",
    "TGLANG_LANGUAGE_OCAML",
    "TGLANG_LANGUAGE_OPENEDGE_ABL",
    "TGLANG_LANGUAGE_PASCAL",
    "TGLANG_LANGUAGE_PERL",
    "TGLANG_LANGUAGE_PHP",
    "TGLANG_LANGUAGE_PL_SQL",
    "TGLANG_LANGUAGE_POWERSHELL",
    "TGLANG_LANGUAGE_PROLOG",
    "TGLANG_LANGUAGE_PROTOBUF",
    "TGLANG_LANGUAGE_PYTHON",
    "TGLANG_LANGUAGE_QML",
    "TGLANG_LANGUAGE_R",
    "TGLANG_LANGUAGE_RAKU",
    "TGLANG_LANGUAGE_REGEX",
    "TGLANG_LANGUAGE_RUBY",
    "TGLANG_LANGUAGE_RUST",
    "TGLANG_LANGUAGE_SAS",
    "TGLANG_LANGUAGE_SCALA",
    "TGLANG_LANGUAGE_SCHEME",
    "TGLANG_LANGUAGE_SHELL",
    "TGLANG_LANGUAGE_SMALLTALK",
    "TGLANG_LANGUAGE_SOLIDITY",
    "TGLANG_LANGUAGE_SQL",
    "TGLANG_LANGUAGE_SWIFT",
    "TGLANG_LANGUAGE_TCL",
    "TGLANG_LANGUAGE_TEXTILE",
    "TGLANG_LANGUAGE_TL",
    "TGLANG_LANGUAGE_TYPESCRIPT",
    "TGLANG_LANGUAGE_UNREALSCRIPT",
    "TGLANG_LANGUAGE_VALA",
    "TGLANG_LANGUAGE_VBSCRIPT",
    "TGLANG_LANGUAGE_VERILOG",
    "TGLANG_LANGUAGE_VISUAL_BASIC",
    "TGLANG_LANGUAGE_WOLFRAM",
    "TGLANG_LANGUAGE_XML",
    "TGLANG_LANGUAGE_YAML",
}

langs = []
samples = []

# -----------------------------------------------------
import os
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import cross_val_score
from sklearn.naive_bayes import MultinomialNB

# path to code samples
folder_path = "./resources"
k = 0

for lang in all_langs:
    file_name = lang[16:].lower() + '.txt'
    file_path = os.path.join(folder_path, file_name)

    if not os.path.exists(file_path):
        print(f"File `{file_name}` was not found!")
        continue

    with open(file_path, 'r', encoding='utf-8') as file:
        sample = file.read()

    if sample == "":
        print(f"File `{file_name}` is empty!")
        continue

    langs.append(lang)
    samples.append(sample)
    k += 1

print()

if not langs or not samples:
    print('Any langs was not founded! Stopped!')
    exit()

print(f"Was founded samples for langs: {k}/{100}\n")

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(samples)

classifier = MultinomialNB()

classifier.fit(X, langs)

# scores = cross_val_score(classifier, X, langs, cv=5)
# print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

def determine(code: str) -> str:
    predicted_lang = classifier.predict(vectorizer.transform([code]))[0]
    return predicted_lang

import time

while True:
    code = input("нажмите что-нибудь:")
    with open('./resources/tests/test.txt', 'r', encoding='utf-8') as file:
        code = file.read()
    
    start_time = time.time()
    predicted_lang = determine(code)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000
    
    print(f"Язык: {predicted_lang}")
    print(f"Время исполнения: {execution_time_ms} мс")