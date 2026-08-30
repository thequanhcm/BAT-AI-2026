@echo off
echo ============================================================
echo STARTING SKILL_BAT_AI - AUTONOMOUS AI WORKFORCE DAEMON
echo ============================================================
echo.
echo Initializing environment variables...
REM Uncomment and set your secret below for production use!
REM set QUANPT1_APPROVAL_SECRET=YOUR_SECRET_HERE

echo Checking for mock_logs directory...
if not exist "mock_logs" mkdir "mock_logs"

echo.
echo Starting Supervisor Daemon...
python -c "import time; from supervisor_daemon import SupervisorDaemon; d = SupervisorDaemon(); d.start(); print('Daemon running. Press Ctrl+C to stop.'); time.sleep(999999)"
pause
