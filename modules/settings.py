from binaryninja import Settings

Settings().register_group("chararr","Char Arrays Plugin")

Settings().register_setting("chararr.Verbosity.infonotif","""
	{
		"title":"Enable Completion Notification",
		"type":"boolean",
		"default":false,
		"description":"When turned on, a notification will alert the user of found char arrays upon completion."
	}
""")

Settings().register_setting("chararr.Verbosity.comments","""
	{
		"title":"Enable Informative Comments",
		"type":"boolean",
		"default":true,
		"description":"When turned on, comments will be added to analyzed targets displaying confidence and size."
	}
""")

Settings().register_setting("chararr.Confidence.threshold","""
	{
		"title":"Re-adjust Confidence Threshold",
		"type":"number",
		"default":100,
		"description":"This is the confidence level that must be exceeded for a type to be redefined as a char array."
	}
""")

Settings().register_setting("chararr.Heuristics.strfunc","""
	{
		"title":"String Function Usage",
		"type":"boolean",
		"default":true,
		"description":"Checks if the target is being passed into string functions."
	}
""")

Settings().register_setting("chararr.Heuristics.indexAccess","""
        {
                "title":"Index Access",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target is being accessed via index."
        }
""")

Settings().register_setting("chararr.Heuristics.stdio","""
        {
                "title":"Stdio Usage",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target is used in stdio functions with file streams."
        }
""")

Settings().register_setting("chararr.Heuristics.fds","""
        {
                "title":"File Descriptor Usage",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target is being passed into functions that use file descriptors."
        }
""")

Settings().register_setting("chararr.Heuristics.exceededSize","""
        {
                "title":"Exceeding Size",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target is of a size larger than its declared type. (For non-void types)"
        }
""")

Settings().register_setting("chararr.Heuristics.terminated","""
        {
                "title":"Null Terminator",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target has a null byte as it's last byte."
        }
""")

Settings().register_setting("chararr.Heuristics.isVoid","""
        {
                "title":"Is Void",
                "type":"boolean",
                "default":true,
                "description":"Checks if the target was analyzed as a void type."
        }
""")

