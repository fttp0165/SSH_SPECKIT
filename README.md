# SSH Client Spec-Kit 專案

## 專案簡介
本專案以 Python 開發，使用 Spec-Kit、Paramiko 實作 SSH 連線功能，並採 TDD 測試流程。

## 功能列表
- [x] SSH 連線
- [x] 待命（保持連線）
- [x] 發送指令
- [x] 關閉連線
- [x] TDD 測試

## 進度表
| 功能           | 狀態   |
| -------------- | ------ |
| SSH 連線       | ✅ 完成 |
| 待命           | ✅ 完成 |
| 發送指令       | ✅ 完成 |
| 關閉連線       | ✅ 完成 |
| TDD 測試       | ✅ 完成 |

## 使用方式
1. 安裝依賴：`spec-kit`, `paramiko`, `pytest`
2. 編輯 `ssh_client.py` 實作 SSH 功能
3. 撰寫 `tests/test_ssh_client.py` 進行 TDD 測試
4. 執行測試：
   ```powershell
   C:/Users/BENNYLIN.SPORTON/.pyenv/pyenv-win/versions/3.12.4/python.exe -m pytest tests
   ```

## 聯絡方式
如需協助請聯絡專案負責人。
