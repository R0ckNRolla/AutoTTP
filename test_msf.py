" make sure all the modules can import/load"
from msf_exploit_autocomplete import exploit
from msf_post_autocomplete import post
from msf_payload_autocomplete import payload
# there may be illegal characters, especially within options class variables
# the import will fail there are illegal characters within class
# print some stuff
print(payload.windows_meterpreter_reverse_https.path)
print(exploit.windows_winrm_winrm_script_exec.path)
print(post.windows_capture_keylog_recorder.path)