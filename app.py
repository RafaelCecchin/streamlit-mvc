import subprocess

def main():
    processes = []
    try:
        streamlit_process = subprocess.Popen(["streamlit", "run", "services/StreamlitService.py", "--server.headless", "true"])
        fastapi_process = subprocess.Popen(["uvicorn", "services.FastAPIService:app", "--port", "8000"])
        processes.extend([streamlit_process, fastapi_process])
        
        for process in processes:
            process.wait()
    except KeyboardInterrupt:
        print("Interrompido. Encerrando servidores...")
        for process in processes:
            process.terminate()
    finally:
        for process in processes:
            process.wait()

if __name__ == '__main__':
    main()