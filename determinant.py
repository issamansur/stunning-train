import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

code_samples = {
    "TGLANG_LANGUAGE_OTHER": "/* Code in another language */\nfunction hello() {\n    console.log('Hello, world!');\n}",
    "TGLANG_LANGUAGE_1S_ENTERPRISE": "// 1C:Enterprise code\nПроцедура Пример()\n    Сообщить(\"Hello, world!\");\nКонецПроцедуры",
    "TGLANG_LANGUAGE_ABAP": "\" ABAP code\nREPORT ZHELLO.\nWRITE: 'Hello, world!'.",
    "TGLANG_LANGUAGE_ACTIONSCRIPT": "// ActionScript code\nfunction hello():void {\n    trace('Hello, world!');\n}",
    "TGLANG_LANGUAGE_ADA": "-- Ada code\nprocedure Hello is\nbegin\n   Put_Line(\"Hello, world!\");\nend Hello;",
    "TGLANG_LANGUAGE_APACHE_GROOVY": "// Apache Groovy code\ndef hello() {\n    println 'Hello, world!'\n}",
    "TGLANG_LANGUAGE_APEX": "// Apex code\npublic class HelloWorld {\n    public static void main(String[] args) {\n        System.debug('Hello, world!');\n    }\n}",
    "TGLANG_LANGUAGE_APPLESCRIPT": "-- AppleScript code\ndisplay dialog \"Hello, world!\"",
    "TGLANG_LANGUAGE_ASP": "' ASP code\n<% Response.Write(\"Hello, world!\") %>",
    "TGLANG_LANGUAGE_ASSEMBLY": "; Assembly code\nsection .data\nhello db 'Hello, world!',0\nsection .text\nglobal _start\n_start:\n    mov eax, 4\n    mov ebx, 1\n    mov ecx, hello\n    mov edx, 13\n    int 0x80\n    mov eax, 1\n    int 0x80",
    "TGLANG_LANGUAGE_AUTOHOTKEY": "; AutoHotkey code\nMsgBox, Hello, world!",
    "TGLANG_LANGUAGE_AWK": "# AWK code\nBEGIN { print \"Hello, world!\" }",
    "TGLANG_LANGUAGE_BASIC": "' BASIC code\nPRINT \"Hello, world!\"",
    "TGLANG_LANGUAGE_BATCH": "@echo off\nREM Batch code\nECHO Hello, world!",
    "TGLANG_LANGUAGE_BISON": "%{ C code %}\n\n/* Bison code */\n\n%}",
    "TGLANG_LANGUAGE_C": "// C code\n#include <stdio.h>\nint main() {\n    printf(\"Hello, world!\\n\");\n    return 0;\n}",
    "TGLANG_LANGUAGE_CLOJURE": "; Clojure code\n(defn hello []\n  (println \"Hello, world!\"))",
    "TGLANG_LANGUAGE_CMAKE": "# CMake code\nmessage(\"Hello, world!\")",
    "TGLANG_LANGUAGE_COBOL": "* COBOL code\n       IDENTIFICATION DIVISION.\n       PROGRAM-ID. HelloWorld.\n       PROCEDURE DIVISION.\n           DISPLAY 'Hello, world!'.\n           STOP RUN.",
    "TGLANG_LANGUAGE_COFFESCRIPT": "// CoffeeScript code\nconsole.log 'Hello, world!'",
    "TGLANG_LANGUAGE_COMMON_LISP": "; Common Lisp code\n(defun hello ()\n  (format t \"Hello, world!~%\"))",
    "TGLANG_LANGUAGE_CPLUSPLUS": "// C++ code\n#include <iostream>\nint main() {\n    std::cout << \"Hello, world!\" << std::endl;\n    return 0;\n}",
    "TGLANG_LANGUAGE_CRYSTAL": "# Crystal code\nputs \"Hello, world!\"",
    "TGLANG_LANGUAGE_CSHARP": "// C# code\nusing System;\nclass Program {\n    static void Main() {\n        Console.WriteLine(\"Hello, world!\");\n    }\n}",
    "TGLANG_LANGUAGE_CSS": "/* CSS code */\nbody {\n    font-size: 16px;\n    color: #333;\n}",
    "TGLANG_LANGUAGE_CSV": "# CSV data\nName, Age, Country\nAlice, 30, USA\nBob, 25, UK\n",
    "TGLANG_LANGUAGE_D": "// D code\nimport std.stdio;\nvoid main() {\n    writeln(\"Hello, world!\");\n}",
    "TGLANG_LANGUAGE_DART": "// Dart code\void main() {\n    print('Hello, world!');\n}",
    "TGLANG_LANGUAGE_DELPHI": "// Delphi code\nprogram HelloWorld;\nbegin\n  writeln('Hello, world!');\nend.",
    "TGLANG_LANGUAGE_DOCKER": "# Dockerfile\nFROM ubuntu\nRUN echo 'Hello, world!'",
    "TGLANG_LANGUAGE_ELIXIR": "# Elixir code\nIO.puts \"Hello, world!\"",
    "TGLANG_LANGUAGE_ELM": "-- Elm code\nimport Html exposing (text)\n\nmain =\n    text \"Hello, world!\"",
    "TGLANG_LANGUAGE_ERLANG": "% Erlang code\n-module(hello).\n-export([world/0]).\nworld() ->\n    io:format(\"Hello, world!~n\").",
    "TGLANG_LANGUAGE_FIFT": "// Fift code\n\n\" Hello, world!\" 42 . cr",
    "TGLANG_LANGUAGE_FORTH": "\\ FORTH code\n: hello  \" Hello, world!\" . ;
    hello",
    "TGLANG_LANGUAGE_FORTRAN": "! Fortran code\nprogram hello\n    print *, 'Hello, world!'\nend program hello",
    "TGLANG_LANGUAGE_FSHARP": "// F# code\nprintfn \"Hello, world!\"",
    "TGLANG_LANGUAGE_FUNC": "// Func code\nfn main() {\n    println!(\"Hello, world!\");\n}",
    "TGLANG_LANGUAGE_GAMS": "$title Example\n$onText\nHello, world!\n",
    "TGLANG_LANGUAGE_GO": "// Go code\npackage main\nimport \"fmt\"\nfunc main() {\n    fmt.Println(\"Hello, world!\")\n}",
    "TGLANG_LANGUAGE_GRADLE": "// Gradle build file\nprintln 'Hello, world!'",
    "TGLANG_LANGUAGE_GRAPHQL": "# GraphQL schema\n\ntype Query {\n  hello: String\n}",
    "TGLANG_LANGUAGE_HACK": "// Hack code\nfunction main(): void {\n  echo \"Hello, world!\";\n}",
    "TGLANG_LANGUAGE_HASKELL": "-- Haskell code\nmain :: IO ()\nmain = putStrLn \"Hello, world!\"",
    "TGLANG_LANGUAGE_HTML": "<!-- HTML code -->\n<!DOCTYPE html>\n<html>\n<head>\n    <title>Hello, world!</title>\n</head>\n<body>\n    <h1>Hello, world!</h1>\n</body>\n</html>",
    "TGLANG_LANGUAGE_ICON": "// Icon code\nprocedure main()\n   write(\"Hello, world!\")\nend",
    "TGLANG_LANGUAGE_IDL": "; IDL code\nvoid hello() {\n    print, 'Hello, world!'\n}",
    "TGLANG_LANGUAGE_INI": "; INI configuration\n[Settings]\nGreeting=Hello, world!",
    "TGLANG_LANGUAGE_JAVA": "// Java code\nclass HelloWorld {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, world!\");\n    }\n}",
    "TGLANG_LANGUAGE_JAVASCRIPT": "// JavaScript code\nfunction hello() {\n    console.log('Hello, world!');\n}",
    "TGLANG_LANGUAGE_JSON": "{\n    \"message\": \"Hello, world!\"\n}",
    "TGLANG_LANGUAGE_JULIA": "# Julia code\nprintln(\"Hello, world!\")",
    "TGLANG_LANGUAGE_KEYMAN": "' Keyman code\nbegin Unicode > use(main)\n+ [CTRL ALT K] > 'Hello, world!'\n",
    "TGLANG_LANGUAGE_KOTLIN": "// Kotlin code\nfun main() {\n    println(\"Hello, world!\")\n}",
    "TGLANG_LANGUAGE_LATEX": "% LaTeX code\ndocumentclass{article}\n\\begin{document}\nHello, world!\n\\end{document}",
    "TGLANG_LANGUAGE_LISP": "; Lisp code\n(format t \"Hello, world!~%\")",
    "TGLANG_LANGUAGE_LOGO": "; Logo code\nprint [Hello, world!]",
    "TGLANG_LANGUAGE_LUA": "-- Lua code\nprint(\"Hello, world!\")",
    "TGLANG_LANGUAGE_MAKEFILE": "# Makefile\nall:\n    @echo 'Hello, world!'",
    "TGLANG_LANGUAGE_MARKDOWN": "# Markdown document\n\n# Hello, world!",
    "TGLANG_LANGUAGE_MATLAB": "% MATLAB code\nfprintf('Hello, world!\\n');",
    "TGLANG_LANGUAGE_NGINX": "# Nginx configuration\nserver {\n    listen 80;\n    server_name localhost;\n    location / {\n        echo 'Hello, world!';\n    }\n}",
    "TGLANG_LANGUAGE_NIM": "# Nim code\necho \"Hello, world!\"",
    "TGLANG_LANGUAGE_OBJECTIVE_C": "// Objective-C code\n#import <Foundation/Foundation.h>\nint main() {\n    NSLog(@\"Hello, world!\");\n    return 0;\n}",
    "TGLANG_LANGUAGE_OCAML": "(* OCaml code *)\nprint_string \"Hello, world!\\n\";",
    "TGLANG_LANGUAGE_OPENEDGE_ABL": "// OpenEdge ABL code\nDISPLAY 'Hello, world!'.",
    "TGLANG_LANGUAGE_PASCAL": "// Pascal code\nprogram HelloWorld;\nbegin\n  writeln('Hello, world!');\nend.",
    "TGLANG_LANGUAGE_PERL": "# Perl code\nprint \"Hello, world!\\n\";",
    "TGLANG_LANGUAGE_PHP": "// PHP code\necho \"Hello, world!\";",
    "TGLANG_LANGUAGE_PL_SQL": "-- PL/SQL code\nBEGIN\n  DBMS_OUTPUT.PUT_LINE('Hello, world!');\nEND;",
    "TGLANG_LANGUAGE_POWERSHELL": "# PowerShell code\nWrite-Host 'Hello, world!'",
    "TGLANG_LANGUAGE_PROLOG": "% Prolog code\n:- initialization(main).\nmain :- write('Hello, world!'), nl.",
    "TGLANG_LANGUAGE_PROTOBUF": "// Protocol Buffers (ProtoBuf) definition\nmessage Hello {\n  required string greeting = 1;\n}",
    "TGLANG_LANGUAGE_PYTHON": "# Python code\nprint(\"Hello, world!\")",
    "TGLANG_LANGUAGE_QML": "// QML code\nimport QtQuick 2.15\nItem {\n    Text { text: 'Hello, world!' }\n}",
    "TGLANG_LANGUAGE_R": "# R code\ncat('Hello, world!\\n')",
    "TGLANG_LANGUAGE_RAKU": "# Raku code\nsay 'Hello, world!';",
    "TGLANG_LANGUAGE_REGEX": "# Regular Expression\npattern = r\"^Hello, world!$\"",
    "TGLANG_LANGUAGE_RUBY": "# Ruby code\nputs 'Hello, world!'",
    "TGLANG_LANGUAGE_RUST": "// Rust code\nfn main() {\n    println!(\"Hello, world!\");\n}",
    "TGLANG_LANGUAGE_SAS": "/* SAS code */\n%put Hello, world!;",
    "TGLANG_LANGUAGE_SCALA": "// Scala code\nobject HelloWorld extends App {\n    println(\"Hello, world!\")\n}",
    "TGLANG_LANGUAGE_SCHEME": "; Scheme code\n(display \"Hello, world!\") (newline)",
    "TGLANG_LANGUAGE_SHELL": "# Shell script\necho 'Hello, world!'",
    "TGLANG_LANGUAGE_SMALLTALK": "\" Smalltalk code\n'Hello, world!' displayNl.",
    "TGLANG_LANGUAGE_SOLIDITY": "// Solidity code\npragma solidity ^0.8.0;\ncontract HelloWorld {\n    function sayHello() public pure returns (string memory) {\n        return 'Hello, world!';\n    }\n}",
    "TGLANG_LANGUAGE_SQL": "-- SQL code\nSELECT 'Hello, world!' AS message;",
    "TGLANG_LANGUAGE_SWIFT": "// Swift code\nprint(\"Hello, world!\")",
    "TGLANG_LANGUAGE_TCL": "# Tcl code\necho \"Hello, world!\"",
    "TGLANG_LANGUAGE_TEXTILE": "# Textile markup\n\np. Hello, world!",
    "TGLANG_LANGUAGE_TL": "# TL code\nHello, world!",
    "TGLANG_LANGUAGE_TYPESCRIPT": "// TypeScript code\nclass HelloWorld {\n    static main() {\n        console.log('Hello, world!');\n    }\n}",
    "TGLANG_LANGUAGE_UNREALSCRIPT": "// UnrealScript code\nclass HelloWorld extends Actor;\nvar() localized string HelloWorldMessage;\nfunction PostBeginPlay() {\n    `log(HelloWorldMessage @ \"\\n\");\n}",
    "TGLANG_LANGUAGE_VALA": "// Vala code\nvoid main() {\n    stdout.printf(\"Hello, world!\\n\");\n}",
    "TGLANG_LANGUAGE_VBSCRIPT": "' VBScript code\nMsgBox \"Hello, world!\"",
    "TGLANG_LANGUAGE_VERILOG": "// Verilog code\nmodule HelloWorld;\ninitial begin\n    $display(\"Hello, world!\");\n    $finish;\nend\nendmodule",
    "TGLANG_LANGUAGE_VISUAL_BASIC": "' Visual Basic code\nSub Main()\n    Console.WriteLine(\"Hello, world!\")\nEnd Sub",
    "TGLANG_LANGUAGE_WOLFRAM": "# Wolfram Language code\nPrint[\"Hello, world!\"]",
    "TGLANG_LANGUAGE_XML": "<!-- XML code -->\n<root>\n    <message>Hello, world!</message>\n</root>",
    "TGLANG_LANGUAGE_YAML": "# YAML data\nmessage: Hello, world!"
}

# Разделите данные на обучающий и тестовый набор
X = list(code_samples.values())
y = list(code_samples.keys())
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Создайте объект CountVectorizer для извлечения признаков из текста
vectorizer = CountVectorizer()

# Преобразуйте обучающий и тестовый текст в матрицы признаков
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Создайте и обучите модель мультиномиальной логистической регрессии
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Предскажите язык для тестовых данных
y_pred = model.predict(X_test_vec)

# Оцените точность модели
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Предскажите язык для нового кода
new_code = ["function suma(a, b) {\n    return a + b;\n}"]
new_code_vec = vectorizer.transform(new_code)
predicted_language = model.predict(new_code_vec)
print(f"Predicted Language: {predicted_language[0]}")
