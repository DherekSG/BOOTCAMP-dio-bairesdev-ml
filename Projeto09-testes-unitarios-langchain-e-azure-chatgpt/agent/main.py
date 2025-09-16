import argparse
from pathlib import Path
from agent.agent import generate_tests_for_file

def main():
    parser = argparse.ArgumentParser(description="Agente de geração de testes (pytest) com LangChain + Azure OpenAI")
    parser.add_argument("--input", "-i", required=True, help="Caminho do arquivo Python de entrada (ex.: examples/math_utils.py)")
    parser.add_argument("--output", "-o", required=True, help="Caminho de saída para o arquivo de testes (ex.: tests/test_math_utils.py)")
    args = parser.parse_args()

    test_code = generate_tests_for_file(args.input)
    out_path = Path(args.output)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(test_code, encoding="utf-8")
    print(f"Arquivo de testes gerado em: {out_path}")

if __name__ == "__main__":
    main()
