---
layout: default
title: Read Property Files Using Resource Bundle
parent: Spring Framework
nav_order: 3
---


``` java

public class ConfigurationUtil {
    private static ResourceBundle resource;
    private static final String defaultConfigurationFileName = "file-in-classpath";
    private static final String NAME1 = "key1";
    public static void loadConfigurations() {
        ConfigurationUtil.resource = ResourceBundle.getBundle(ConfigurationUtil.defaultConfigurationFileName);
    }
    public static String getPropName() {
        return resource.getString(ConfigurationUtil.NAME1);
    }
}
```
